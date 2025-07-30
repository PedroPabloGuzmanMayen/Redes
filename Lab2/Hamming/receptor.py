import socket



polinomio = "1001" #Polinomio a utlizar para decodificar
# Decodificación con Hamming
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

# Detección de errores con CRC
def detectar_errores_CRC(mensaje: str):
    result = mensaje
    temp = ""
    while ( len(result) >= len(polinomio)):
        for i in range(len(polinomio)):
            temp +=(str(int(result[i]) ^ int(polinomio[i])))
        if temp[0] == '0':
            result = temp[1:] + result[len(polinomio):]
        else:
            result = temp + result[len(polinomio):]
        print("Result: ", result)
        temp = ""

    if "1" in result:
        return True
    else:
        return False
    
"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 9999))
    print("Escuchando solicitudes ...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Se recibió un mensaje! ")
        while True: 
            data = conn.recv(1024)
            if not data:
                break
            print(f"Mensaje recibido: {data.decode()} ")

"""

print(detectar_errores_CRC("10011001"))


