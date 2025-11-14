# Lab 7 

## Dependencias
- librdkafka

## ¿Cómo ejecutar el lab?

En la raíz del repositorio, ejecutar la primera vez:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Para ejecutar el productor: 

```sh
source .venv/bin/activate
python producers/sensor_simulator.py --topic 13245 --bootstrap-server iot.redesuvg.cloud:9092 --interval 20
```
Para ejecutar el consumidor y graficador:

```sh
source .venv/bin/activate
python consumers/consumer_plotter.py --topic 13245 --bootstrap-server iot.redesuvg.cloud:9092
```

## Estructura del Lab 7

```txt
Lab10/
├── README.md
├── .gitignore
├── requirements.txt
├── producers/
│ ├── sensor_simulator.py # productor principal 
│ ├── encode_decode.py # funciones encode/decode 
│ └── config.py 
├── consumers/
│ ├── consumer_plotter.py # consumidor que acumula y grafica 
│ ├── decoder.py # wrapper que usa encode_decode para decodificar
│ └── config.py
├── dashboard/
│ └── app.py # servidor web simple [Streamlit la vieja confiable] 
├── docs/
│ ├── slides_sources/ # el slide
│ └── screenshots/ # capturas de pantalla de lo que vayamos sacando 
└── outputs/
```


Pasos [Nuestra mini guia para ir documentando en la presentacion - Borrar el listado al final]: 

1. (Código: captura del archivo `producers/sensor_simulator.py` o fragmento clave)
2. (Ejecución: captura del productor enviando mensajes a Kafka — terminal con `producer.send` o `print` de mensajes)
3. (Código: captura del archivo `consumers/consumer_plotter.py` o fragmento clave que procesa mensajes)
4. (Ejecución: captura del consumidor recibiendo y decodificando mensajes)
5. (Gráfica: captura de la ventana o página con las gráficas actualizadas en vivo)
6. (Encode/Decode: captura de tests unitarios `tests/test_encode_decode.py` y resultado de `pytest`)
7. (Restricción 3 bytes: captura mostrando el payload binario (3 bytes) enviado)
8. (Comparativa: captura o tabla breve que muestre ventajas/desventajas del enfoque Pub/Sub con Kafka)
9. (Screenshots finales: slide con resumen y conclusiones)

