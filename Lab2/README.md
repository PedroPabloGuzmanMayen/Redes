# Laboratorio 2 - Redes
---
Pedro Guzmán - 22111
Gustavo Cruz - 22779

---

## Código de Hamming – Emisor

### Implementación

Se desarrolló una implementación en Julia del emisor del código de Hamming, siguiendo la relación:

(m + r + 1) ≤ 2^r

donde:
- m = cantidad de bits del mensaje original
- r = cantidad mínima de bits de paridad necesarios

La implementación:
- Calcula el número de bits de paridad necesarios.
- Inserta bits de paridad en posiciones 2^i.
- Calcula los valores de paridad aplicando xor entre los bits correspondientes.

---

### Pruebas realizadas 
#### (emisor)

### PRUEBA 1

Mensaje original: `1010`  
Número de bits de paridad necesarios: `3`  
Bits con espacios de paridad: `0010010`  
Mensaje codificado con Hamming: `1011010`

### PRUEBA 2

Mensaje original: `110011`  
Número de bits de paridad necesarios: `4`  
Bits con espacios de paridad: `0010100011`  
Mensaje codificado con Hamming: `1011100011`

### PRUEBA 3

Mensaje original: `1001101`  
Número de bits de paridad necesarios: `4`  
Bits con espacios de paridad: `00100010101`  
Mensaje codificado con Hamming: `01110010101`

#### (receptor)

---

## Pruebas de detección/corrección

### Sin errores

Para esta prueba, se toma el mensaje codificado generado por el emisor y se pasa tal cual al receptor. La respuesta esperada es el mensaje original sin cambios.

Resultados esperados:
- PRUEBA 1:  
  Entrada al receptor: `1011010`  
  Salida esperada: ``

- PRUEBA 2:  
  Entrada al receptor: `1011100011`  
  Salida esperada: ``

- PRUEBA 3:  
  Entrada al receptor: `01110010101`  
  Salida esperada: ``

---

### Con un error

Para esta prueba, se modifica un bit del mensaje codificado antes de pasarlo al receptor. El receptor debe detectar y corregir el error, e indicar la posición modificada.


---

### Con dos errores

En esta prueba se alteran dos bits. El receptor debe detectar que el mensaje contiene errores.

---

## ¿Es posible manipular los bits de tal forma que el algoritmo no detecte el error?

Sí. En el código de Hamming, si se alteran dos bits específicos del mensaje codificado, el patrón que generan puede coincidir con el patrón de un error en otra posición o incluso parecer que el mensaje está correcto. Esto puede hacer que el receptor no detecte el error, o corrija mal un bit que no estaba dañado.

---

## Ventajas y desventajas del código de Hamming

Ventajas:
- Corrige errores de 1 solo bit.
- Detecta errores de 2 bits (aunque no los puede corregir).
- Se puede implementar fácilmente aplicando XOR y manipulaciones de bits.

Desventajas:
- No puede corregir errores múltiples.
- Requiere varios bits de paridad extra (r crece logarítmicamente).
- Más complejo que un bit de paridad simple o CRC si solo se requiere detección.

---

## Conclusiones
