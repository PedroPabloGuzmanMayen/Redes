# Reporte 1

## Integrantes

- Gustavo Cruz 22779
- Pedro Guzmán 22111

## Integrantes adicionales 

- Gabriela Mazariegos 22513
- Santiago Pereira 22318


## Ejercicio 1

- **Forma de traducir el morse:**: usando un software en línea que genera el audio y poniéndolo en la llamada al receptor
- **Forma de traducir Blaudot:** usado físicamente un sonido más grave y uno más agudo (somatar el escritorio para los + y golpear una estructura metálica para los 0)
### Mensaje 1

- Emisor: Pedro Guzmán  
- Mensaje original: HOLA MUNDO  
- Baudot:  
  H → 10100  
  O → 01100  
  L → 11100  
  A → 00011  
  (espacio)  
  M → 10011  
  U → 00100  
  N → 10111  
  D → 00010  
  O → 01100  
- Secuencia completa:  
  `10100 01100 11100 00011`  
  `10011 00100 10111 00010 01100`  
- Mensaje decodificado: HOLA MUNRO  
- Errores: Letra "D" interpretada como "R" por cambio de un bit.  

---

### Mensaje 2

- Emisor: Gustavo Cruz  
- Mensaje original: PRUEBA123    
- Baudot:  
  Letras:  
  P → 01101  
  R → 01010  
  U → 00100  
  E → 00001  
  B → 11000  
  A → 00011  
  FIGS → 11011  
  1 → 10111  
  2 → 10011  
  3 → 00010  
- Secuencia completa:  
  `01101 01010 00100 00001 11000 00011`  
  `11011 10111 10011 00010`  
- Mensaje decodificado: PRUEBA123  
- Errores: No hubo errores  

---

### Mensaje 3

- Emisor: Gustavo Cruz  
- Mensaje original: CODIGO ROTO  
- Baudot :  
  C → 01110  
  O → 01100  
  D → 00010  
  I → 01011  
  G → 11010  
  O → 01100  
  (espacio)  
  R → 01010  
  O → 01100  
  T → 10000  
  O → 01100  
- Secuencia completa:  
  `01110 01100 00010 01011 11010 01100`  
  `01010 01100 10000 01100`  
- Mensaje decodificado: CODIGO ROTO  
- Errores: No hubo errores    


### Mensaje 4

- Emisor: Gustavo Cruz  
- Mensaje original: Hola equipo  
- Mensaje en morse: .... --- .-.. .- / . --.- ..- .. .--. ---  
- Mensaje decodificado: Hola equlpo  
- Errores: Letra "i" fue interpretada como "l", por lo que "equipo" se leyó como "equlpo".  



### Mensaje 5

- Emisor: Pedro Guzmán  
- Mensaje original: Lunes sin sol  
- Mensaje en morse: .-.. ..- -. . ... / ... .. -. / ... --- .-..  
- Mensaje decodificado: Lunes sin sol  
- Errores: No hubo errores  


### Mensaje 6

- Emisor: Gustavo Cruz  
- Mensaje original: Código roto  
- Mensaje en morse: -.-. --- -.. .. --. --- / .-. --- - ---  
- Mensaje decodificado: Código roto  
- Errores: La letra “i” fue omitida; la palabra "Código" se interpretó incorrectamente.  

### ¿Cuál esquema fue más fácil? ¿Más difícil?

- El esquema más fácil de escribir fue el código morse pues tiene una escritura sencilla y mensajes largos pueden escribirse de una forma más reducida. El código de Baudot tenía una escritura y forma de representación más compleja. 
- En cuanto a descifrar el mensaje, fue más sencillo de entender Baudot debido a que se hicimos un protocolo en el cuál había dos sonidos 

### ¿Con cuál ocurren menos errores?

- Solo se uso código Morse, no se cometieron tantos errores debido a que la mayoría del tiempo el software generaa los audios de forma limpia aunque a ve
ces era difícil identifcar las letras de forma correcta a la primera. El de Blaudot fue más fácil de identificar debido a que se utilizaron 2 sonidos distintos bastante identificables para representarlo. 

## Ejercicio 2

---

Para reproducir los audios en la página, se recomienda copiar el mensaje original y reproducirlo a una velocidad de "5".

---

### Mensaje 1

- Emisor: Pedro Guzmán
- Mensaje original: No vino Chen
- Mensaje en morse: . .-.. / .-.. .. -.-.
- Medio de transmisión: generador de audio online. [Link aquí](https://morsecode.world/international/translator.html)
- Mesnaje decodificado: No vino Chen
- Errores: No hubo errores


### Mensaje 2

- Emisor Gustavo Cruz
- Mensaje original: Terminemos la tarea
- Mensaje en morse: - . .-. -- .. -. . -- --- ... / .-.. .- / - .- .-. . .-
- Medio de transmisión: audio de whatsapp generado por softare online. [Link aquí](https://morsecode.world/international/translator.html)
- Mensaje decodificado: Terminaron
- Errores: La cadena original tenía 17 caracteres, se identificaron solamente 12 y solo 6 de forma correcta.



### Mensaje 3

* Emisor: Pedro Guzmán
* Mensaje original: Hola mundo en morse
* Mensaje en morse: .... --- .-.. .- / -- ..- -. -.. --- / . -. / -- --- .-. ... .
* Medio de transmisión: audio de whatsapp generado por softare online. [Link aquí](https://morsecode.world/international/translator.html)
* Mensaje decodificado: Hola mundo en morse
* Errores: No hubo errores



### Mensaje 4

* Emisor: Gustavo Cruz
* Mensaje original: Juga Clair Obscur
* Mensaje en morse: .--- ..- --. .- / -.-. .-.. .- .. .-. / --- -... ... -.-. ..- .-.
* Medio de transmisión: audio de whatsapp generado por softare online. [Link aquí](https://morsecode.world/international/translator.html)
* Mensaje decodificado: Juga Clair Obscur
* Errores: No hubo errores



### Mensaje 5

* Emisor: Pedro Guzmán
* Mensaje original: Ganaron los rojos
* Mensaje en morse: --. .- -. .- .-. --- -. / .-.. --- ... / .-. --- .--- --- ...
* Medio de transmisión: audio de whatsapp generado por softare online. [Link aquí](https://morsecode.world/international/translator.html)
* Mensaje decodificado: Ganaron los rojos
* Errores: No hubo errores



### Mensaje 6

* Emisor: Gustavo Cruz
* Mensaje original: Cómo funciona Baudot
* Mensaje en morse: -.-. --- -- --- / ..-. ..- -. -.-. .. --- -. .- / -... .- ..- -.. --- -
* Medio de transmisión: audio de whatsapp generado por softare online. [Link aquí](https://morsecode.world/international/translator.html)
* Mensaje decodificado: Com funciona Baudot
* Errores: Se omitió la tilde en "cómo", y la palabra "funciona" fue decodificada con error en una letra.


## ¿Qué dificultades involucra el enviar un mensaje de esta forma “empaquetada”?

- Realmente no tuvimos dificultades pues el software que usamos generaba el audio de forma correcta y limpia, sin embargo un potencial problema puede surgir cuando se codifique el mensaje de forma manual con objetos físicos pues puede ser que los micrófonos de los dispositivos no sean capaces de capturar los sonidos de forma correcta. 


## Ejercicio 3

- *Conmutador: * Pedro Guzmán
- *Clientes :* Gustavo Cruz, Gabriela Mazariegos, Santiago Pereira

### ¿Qué posibilidades incluye la introducción de un conmutador en el sistema?

-  Introduce la posibilidad de tener a un ente externo que revise los mensajes de una mejor manera y sea capaz de correjir errores en estos.
-  
### ¿Qué ventajas/desventajas se tienen al momento de agregar más conmutadores al sistema?

- Ventajas: la posibilidad de correjir errores o evitar perdida de información
- Desventajas: posiblemente mayores costos de implemetnación

### Qué esquema (código) fue más fácil de transmitir y por qué?¿Qué esquema (código) fue más difícil de transmitir y por qué?

- Solamente se utilizó código morse debido a que los integrantes coincidieron en que este código tenía una escritura/representación más sencilla

### ¿Qué esquema tuvo menos errores (incluir datos que lo evidencien)?

- Solamente se uso el morse, hubieron algunos errores que se detallan a continuación:

#### Mensaje 1

- Original: Hola como estás
- Mensaje identificado por el conmutador: Hola
- Solamente se logró identifcar una cadena debido a que el mensaje en código morse fue representado usando sonidos cotidianos que no eran fácilmente identificables

#### Mensaje 2

- Original: Es para Gustavo
- Identificado: Es para Gustavo
- Se identificó de forma correcta debido a que el código fue generado con un software que generaba el sonido del mensaje de forma más clara y entendible.

#### Mensaje 3

- Original: Hola mundo
- Identificado: Hola mundo
- Se identificó de forma correcta debido a que fue enviado con un software que generaba un sonido claro e identificable

El código morse demostró ser un buen esquema para enviar mensajes pues la mayoría de ellos fueron identificables. 

### ¿Qué dificultades involucra el enviar un mensaje de forma “empaquetada”?

Que a veces se puede perder información debido a errores de los dispositivos de transmición, por ejemplo cuando alguien grababa su mensaje usado objetos cotidianos, a veces el micrófono del dispositivo no capturaba de forma correcta los sonidos.


### Qué ventajas/desventajas se tienen al momento de agregar más conmutadores al sistema?

- Ventajas: más clientes pueden enviar más mensajes al mismo tiempo
- Desventajas: puede ser más costoso

### ¿Qué posibilidades incluye la introducción de un conmutador en el sistema?

- Da la posibilidad de correjir errores en la transmisión del mensaje y mejorar la calidad de este.


### Protocolo utilizado

- El mensaje debía escribirse o representarse usando código morse
- Si el cliente 1 quería enviarle un mensaje al cliente 2, debía enviar su audio el conmutador y luego un mensaje en el que expresara a que cliente iba dirigido el mensaje
- El conmutador enviaba un 0 a los clientes si estaba libre, cuando se ocupaba enviaba un 1 y el cliente debía esperar a que el 0 se enviara nuevamente.

  






