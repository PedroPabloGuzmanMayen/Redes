def detectar_y_corregir(mensaje: str, r: int):


    n = len(mensaje)
    bits = list(mensaje)
    bits.reverse() # Invertir el orden de la cadena
    error_pos = 0
    for i in range(r):
        pos = 2 ** i
        xor = 0
        for j in range(1, n + 1):
            if j & pos:
                xor ^= int(bits[j - 1])
        if xor:
            error_pos += pos

    if error_pos == 0:
        return mensaje, "No hay errores"
    elif error_pos <= n:
        bits[error_pos - 1] = '1' if bits[error_pos - 1] == '0' else '0'
        bits.reverse()
        return ''.join(bits), f"Se corrigió un error en la posición {error_pos}"
    else:
        return mensaje, "Hay 2 o más errores: no se pueden corregir"


print("\n--- ¨Pruebas ---")
mensajes = [
    "10101010111",  # Mensaje sin error
    "1110001",      # Mensaje con un error
    "110110011001"  # Mensaje sin error
]

rs = [4, 3, 4]

for m, r in zip(mensajes, rs):
    resultado, info = detectar_y_corregir(m, r)
    print(f"Mensaje: {m}")
    print(f"Resultado: {resultado}")
    print(f"Info: {info}\n")



