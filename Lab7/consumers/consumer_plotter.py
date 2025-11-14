"""
Uso:
python -m consumers.consumer_plotter --topic 338800
"""

import argparse
import logging
import signal
import sys
import time
from collections import deque, Counter

import matplotlib.pyplot as plt
from confluent_kafka import Consumer, KafkaException

from consumers.decoder import decode_message
from consumers import config as cfg

# Logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger('consumer_plotter')

running = True


def signal_handler(sig, frame):
    global running
    logger.info('SIGINT/SIGTERM recibido — cerrando consumidor...')
    running = False


def make_consumer(bootstrap_servers, group_id, auto_offset):
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'group.id': group_id,
        'auto.offset.reset': auto_offset
    }
    return Consumer(conf)


def setup_plot(max_points):
    plt.ion()
    fig, (ax_t, ax_h, ax_w) = plt.subplots(3, 1, figsize=(9, 8), gridspec_kw={'height_ratios': [3, 3, 2]})
    fig.suptitle('Telemetría - Temperatura / Humedad / Direcciones viento')

    ax_t.set_ylabel('Temperatura (°C)')
    ax_t.set_ylim(0, 120)
    ax_t.grid(True)

    ax_h.set_ylabel('Humedad (%)')
    ax_h.set_ylim(0, 110)
    ax_h.grid(True)

    ax_w.set_ylabel('Frecuencia (conteo)')
    ax_w.set_xlabel('Dirección viento')
    ax_w.grid(axis='y')

    # Inicializar líneas vacías
    t_line, = ax_t.plot([], [], label='Temperatura')
    h_line, = ax_h.plot([], [], label='Humedad', color='tab:orange')

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig, ax_t, ax_h, ax_w, t_line, h_line


def update_plot(ax_t, ax_h, ax_w, t_line, h_line, timestamps, temps, hums, wind_counts, wind_labels):
    if len(timestamps) > 0:
        x = list(range(len(timestamps)))
        t_line.set_data(x, list(temps))
        h_line.set_data(x, list(hums))

        ax_t.set_xlim(0, max(10, len(timestamps)))
        ax_h.set_xlim(0, max(10, len(timestamps)))

    counts = [wind_counts.get(w, 0) for w in wind_labels]
    ax_w.clear()
    ax_w.bar(wind_labels, counts)
    ax_w.set_ylabel('Frecuencia (conteo)')
    ax_w.grid(axis='y')

    plt.pause(0.001)


def main():
    global running

    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', required=True)
    parser.add_argument('--bootstrap-server', default=cfg.DEFAULT_BOOTSTRAP_SERVER)
    parser.add_argument('--group-id', default=cfg.DEFAULT_GROUP_ID)
    parser.add_argument('--mode', choices=['matplotlib', 'console'], default='matplotlib')
    parser.add_argument('--auto-offset', choices=['earliest', 'latest'], default=cfg.DEFAULT_AUTO_OFFSET)
    parser.add_argument('--max-points', type=int, default=cfg.MAX_POINTS)
    args = parser.parse_args()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    consumer = make_consumer(args.bootstrap_server, args.group_id, args.auto_offset)
    consumer.subscribe([args.topic])
    logger.info('Suscrito al topic %s en %s (grupo=%s)', args.topic, args.bootstrap_server, args.group_id)

    max_points = args.max_points
    timestamps = deque(maxlen=max_points)
    temps = deque(maxlen=max_points)
    hums = deque(maxlen=max_points)
    wind_counts = Counter()

    if args.mode == 'matplotlib':
        fig, ax_t, ax_h, ax_w, t_line, h_line = setup_plot(max_points)
        wind_labels = ['N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE']

    try:
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                # No hay mensajes en este intervalo
                continue
            if msg.error():
                # Manejo simple de errores
                logger.error("Error de Kafka: %s", msg.error())
                continue

            try:
                decoded = decode_message(msg.value())
                if decoded is None:
                    logger.warning("Mensaje no reconocido/ignorado (no JSON ni compact)")
                    continue
            except Exception as e:
                logger.exception("Fallo al decodificar mensaje: %s", e)
                continue

            ts = int(decoded.get('timestamp', int(time.time())))
            temp = float(decoded.get('temperatura', 0.0))
            hum = int(decoded.get('humedad', 0))
            wind = decoded.get('direccion_viento', 'UNK')

            # Acumular
            timestamps.append(ts)
            temps.append(temp)
            hums.append(hum)
            wind_counts[wind] += 1

            if args.mode == 'console':
                print(f"[{time.strftime('%H:%M:%S', time.localtime(ts))}] t={temp:.2f}°C h={hum}% w={wind}")
            else:
                update_plot(ax_t, ax_h, ax_w, t_line, h_line, timestamps, temps, hums, wind_counts, wind_labels)

    except KeyboardInterrupt:
        logger.info('Interrupción de teclado detectada — cerrando...')
    except KafkaException as ke:
        logger.exception('KafkaException: %s', ke)
    finally:
        logger.info('Cerrando consumidor y liberando recursos...')
        try:
            consumer.close()
        except Exception:
            pass
        if args.mode == 'matplotlib':
            logger.info('Mantener ventana abierta 2s antes de salir...')
            plt.ioff()
            plt.show(block=False)
            time.sleep(2)

main()

