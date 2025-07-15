# Introducción a wireshark

- Pedro Pablo Guzmán Mayen 22111

## Parte 1

### Creación del perfil en wireshark

![Ejercicio1](Ejercicio1.png)

### Descargar el archivo

![Ejercicio2](Ejercicio2.png)

### Abrir el archivo descargado

![Ejercicio3](Ejercicio3.png)

### Aplicar el formato Time of Day

![Ejercicio4](Ejercicio4.png)

### Agregar una columna con la longitud del protocolo

![Ejercicio5](Ejercicio5_1.png)

![Ejercicio5](Ejercicio5_2.png)

### Eliminar la columna longitud

![Ejercicio6](Ejercicio6_1.png)

![Ejercicio6](Ejercicio6_2.png)

### Aplicar un esquema de paneles diferente

![Ejercicio7](Ejercicio7.png)

### Aplicar regla de color para el protocolo TCP

![Ejercicio8](Ejercicio8_1.png)

![Ejercicio8](Ejercicio8_2.png)

### Aplicar un filtro

![Ejercicio9](Ejercicio9.png)

![Ejercicio9](Ejercicio9_1.png)

### Desactivar las interfaces 

![Ejercicio10](Ejercicio10.png)

![Ejercicio10](Ejercicio10_1.png)


## Parte 2

### Usar el comando ipconfig o ifconfig

![Ejercicio11](Ejercicio11.png)

El comando ipconfig muestra como la computadora está conectada a la red y cuáles interfaces están activas. En mi caso se muestra que tengo activas las interfaces virtuales de WSL y VirtualBox las cuáles sirven para que mi computadora se comunique con dichos servicios. También se puede ver la interfaz de wifi y se muestra la ip que mi router me asignó. 



### Capturar información

![Ejercicio11](Ejercicio11_2.png)




## Parte 3

### Captura de la solicitud http

![Ejercicio12](Ejercicio12.png)

Las solicitudes al sitio indicado son las primeras en la lista

![Ejercicio12](Ejercicio12_1.png)

### ¿Qué versión de HTTP está ejecutando su navegador?

- El navegador ejecuta HTTP1.1

### ¿Qué versión de HTTP está ejecutando el servidor?

- También ejecuta HTTP1.1
### ¿Qué lenguajes (si aplica) indica el navegador que acepta a el servidor?

- No se indica que lengujes se aceptan.

### ¿Cuántos bytes de contenido fueron devueltos por el servidor?

- El servidor devolvió 3568 bytes


### En el caso que haya un problema de rendimiento mientras se descarga la página, ¿En que elementos de la red convendría “escuchar” los paquetes? ¿Es conveniente instalar Wireshark en el servidor? Justifique.

- si sería conveniente también escuchar las peticiones en el servidor 

### Referencias

- ![https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/ipconfig](https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/ipconfig)


