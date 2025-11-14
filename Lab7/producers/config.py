# producers/config.py

DEFAULT_BOOTSTRAP_SERVER = 'iot.redesuvg.cloud:9092'
DEFAULT_MIN_INTERVAL = 15  
DEFAULT_MAX_INTERVAL = 30 

# Mapeo para dirección del viento
WIND_DIRECTIONS = ['N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE']
WIND_TO_CODE = {d: i for i, d in enumerate(WIND_DIRECTIONS)}
CODE_TO_WIND = {i: d for i, d in enumerate(WIND_DIRECTIONS)}

# Rango de sensores
TEMP_MIN = 0.0
TEMP_MAX = 110.0
HUM_MIN = 0
HUM_MAX = 100
