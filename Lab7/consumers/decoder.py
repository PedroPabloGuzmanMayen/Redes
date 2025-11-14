"""
Salida esperada:
{
  'timestamp': int_unix_seconds,
  'temperatura': float,
  'humedad': int,
  'direccion_viento': str
}
"""
import json
import time
from producers.encode_decode import decode_sensor_payload

def decode_message(value: bytes) -> dict:
    """
    Recibe `value` (bytes) desde Kafka y devuelve dict normalizado.
    """
    if value is None:
        return None

    # Si es exactamente 3 bytes asumimos _compact_
    if isinstance(value, (bytes, bytearray)) and len(value) == 3:
        payload = decode_sensor_payload(value)
        # Es posible que el payload no incluya timestamp -> añadimos uno local
        payload.setdefault('timestamp', int(time.time()))
        return payload

    # decodificar como JSON utf-8
    try:
        text = value.decode('utf-8')
        data = json.loads(text)
        # Normalizar nombres por si vienen con keys distintos
        normalized = {
            'timestamp': int(data.get('timestamp', int(time.time()))),
            'temperatura': float(data.get('temperatura', data.get('temp', 0.0))),
            'humedad': int(data.get('humedad', data.get('hum', 0))),
            'direccion_viento': data.get('direccion_viento', data.get('wind', 'UNK'))
        }
        return normalized
    except Exception:
        # Si falla json, devolvemos None para ignorar el mensaje
        return None

