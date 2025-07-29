polinomio = "1001"
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

def detectar_errores_CRC(mensaje: str):
    result = mensaje
    temp = ""
    while ( len(result) > len(polinomio)):
        for i in range(len(polinomio)):
            temp += str(int(result[i]) ^ int(polinomio[i]))

        print(temp)

        if temp[0] == '0':
            result = temp[1:] + mensaje[-(len(result) - len(polinomio)):]
        else: 
            result = temp + mensaje[-(len(result) - len(polinomio)):]
        temp = ""

    if "1" in result:
        return True
    else:
        return False
    


print(detectar_errores_CRC("0110110"))




