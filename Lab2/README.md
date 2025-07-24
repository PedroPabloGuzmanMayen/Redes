# Laboratorio 2 - Redes
---
Pedro Guzmán - 22111
Gustavo Cruz - 22779

---
## Correción de errores

Para la correción de errores se utilizó el algoritmo de Hamming

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

La parte del receptor se hizo en python. Esta función hace lo siguiente: 

- Recibe el mensaje original y el número de bits redundantes que hay en el mensaje
- Recorre las posiciones de redundancia y verifica que la operación XOR entre todas las posiciones que influyen en el bit de redundancia sea igual a 0
- Si se cumple indica quehay error y lo arregla

Para ejecutar: 

```bash
cd Lab2
cd Hamming
julia emisor.jl
python(indicar version) receptor.py
```


---

### Pruebas realizadas 
#### Emisor

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

#### Receptor

### Prueba 1 (0 errores)
Mensaje: 10101010111
Resultado: 10101010111
Info: No hay errores

### Prueba 2 (1 error)
Mensaje: 1110001
Original: 1100001
Resultado: 1100001
Info: Se corrigió un error en la posición 5

### Prueba 3 (2 o más)

Mensaje: 110110011001
Resultado: 110110111001
Info: Se corrigió un error en la posición 6

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
