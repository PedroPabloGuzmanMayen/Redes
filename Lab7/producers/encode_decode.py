from typing import Dict
from producers import config 

from typing import Dict
from producers.config import WIND_TO_CODE, CODE_TO_WIND, TEMP_MIN, TEMP_MAX, HUM_MIN, HUM_MAX
TEMP_SCALE = 100  
MAX_TEMP_SCALED = (1 << 14) - 1  


def encode_sensor_payload(temperature: float, humidity: int, wind_dir: str) -> bytes:
    """Recibe valores (temperature float en °C, humidity int 0-100, wind_dir string) y devuelve 3 bytes."""
    # Clip a rangos válidos
    if temperature < config.TEMP_MIN:
        temperature = config.TEMP_MIN
    if temperature > config.TEMP_MAX:
        temperature = config.TEMP_MAX

    if humidity < config.HUM_MIN:
        humidity = config.HUM_MIN
    if humidity > 127:  # 7 bits max
        humidity = 127

    temp_scaled = int(round(temperature * TEMP_SCALE))
    if temp_scaled > MAX_TEMP_SCALED:
        temp_scaled = MAX_TEMP_SCALED

    wind_code = WIND_TO_CODE.get(wind_dir)
    if wind_code is None:
        raise ValueError(f"Dirección de viento desconocida: {wind_dir}")

    # Empaquetado: temp (14) | hum (7) | wind (3)
    payload_int = (temp_scaled << 10) | (int(humidity) << 3) | (wind_code & 0x7)
    return payload_int.to_bytes(3, 'big')


def decode_sensor_payload(payload: bytes) -> Dict:
    """Decodifica 3 bytes a un dict {'temperatura':float,'humedad':int,'direccion_viento':str}"""
    if not isinstance(payload, (bytes, bytearray)):
        raise TypeError("Payload debe ser bytes")
    if len(payload) != 3:
        raise ValueError("Payload debe tener exactamente 3 bytes")

    payload_int = int.from_bytes(payload, 'big')

    wind_code = payload_int & 0x7
    humidity = (payload_int >> 3) & 0x7F  
    temp_scaled = (payload_int >> 10) & 0x3FFF  

    temperature = temp_scaled / TEMP_SCALE
    wind_dir = CODE_TO_WIND.get(wind_code, 'UNK')

    return {
        'temperatura': round(temperature, 2),
        'humedad': int(humidity),
        'direccion_viento': wind_dir
    }
