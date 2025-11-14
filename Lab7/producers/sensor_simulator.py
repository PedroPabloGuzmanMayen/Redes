"""
Ejecución: 
python producers/sensor_simulator.py --topic 12345 --bootstrap-server iot.redesuvg.cloud:9092 --mode compact
"""
import argparse
import json
import logging
import random
import signal
import sys
import time

from confluent_kafka import Producer

import config
from encode_decode import encode_sensor_payload

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger('sensor_sim')

running = True


def signal_handler(sig, frame):
    global running
    logger.info('SIGINT/SIGTERM recibido — cerrando...')
    running = False


def generate_sample(mean_temp, std_temp, mean_hum, std_hum):
    temp = random.gauss(mean_temp, std_temp)
    temp = max(config.TEMP_MIN, min(config.TEMP_MAX, temp))

    hum = random.gauss(mean_hum, std_hum)
    hum = int(round(max(config.HUM_MIN, min(config.HUM_MAX, hum))))

    wind = random.choice(config.WIND_DIRECTIONS)

    return temp, hum, wind


def delivery_report(err, msg):
    if err is not None:
        logger.error("Entrega fallida: %s", err)
    else:
        logger.debug("Mensaje entregado a %s [%d]", msg.topic(), msg.partition())


def main():
    global running

    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', required=True)
    parser.add_argument('--bootstrap-server', default=config.DEFAULT_BOOTSTRAP_SERVER)
    parser.add_argument('--mode', choices=['json', 'compact'], default='json')
    parser.add_argument('--min-interval', type=float, default=config.DEFAULT_MIN_INTERVAL)
    parser.add_argument('--max-interval', type=float, default=config.DEFAULT_MAX_INTERVAL)
    parser.add_argument('--mean-temp', type=float, default=25.0)
    parser.add_argument('--std-temp', type=float, default=5.0)
    parser.add_argument('--mean-hum', type=float, default=50.0)
    parser.add_argument('--std-hum', type=float, default=10.0)
    parser.add_argument('--key', default='sensor1')

    args = parser.parse_args()

    if args.min_interval > args.max_interval:
        parser.error("min-interval no puede ser mayor que max-interval")

    producer = Producer({
        'bootstrap.servers': args.bootstrap_server
    })

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info("Iniciando productor en topic=%s modo=%s", args.topic, args.mode)

    try:
        while running:
            temp, hum, wind = generate_sample(args.mean_temp, args.std_temp, args.mean_hum, args.std_hum)
            timestamp = int(time.time())

            if args.mode == 'json':
                payload = {
                    'timestamp': timestamp,
                    'temperatura': round(temp, 2),
                    'humedad': hum,
                    'direccion_viento': wind
                }
                data = json.dumps(payload).encode('utf-8')
                logger.info("Enviado JSON: %s", payload)

            else:
                data = encode_sensor_payload(temp, hum, wind)
                logger.info("Enviado COMPACT (hex): %s => t=%.2f h=%d w=%s",
                            data.hex(), temp, hum, wind)

            producer.produce(
                args.topic,
                key=args.key.encode('utf-8'),
                value=data,
                callback=delivery_report
            )

            producer.poll(0)

            sleep_for = random.uniform(args.min_interval, args.max_interval)
            time.sleep(sleep_for)

    except Exception as e:
        logger.exception("Error en el productor: %s", e)
    finally:
        logger.info("Vaciando cola y cerrando productor...")
        producer.flush()
        logger.info("Productor cerrado.")


main()

