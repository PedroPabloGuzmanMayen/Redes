import socket



polinomio = "1001" #Polinomio a utlizar para decodificar
# Decodificación con Hamming
def detectar_y_corregir(mensaje: str):


    bit_extra_recibido = int(mensaje[0])
    datos = mensaje[1:]

    n = len(datos)
    bits = list(datos)
    bits.reverse() # Invertir el orden de la cadena
    error_pos = 0

    r = 0
    while (n - r) + r + 1 > 2**r:  # (m+r+1 > 2^r)
        r += 1
    print("R:", r)
    for i in range(r):
        pos = 2 ** i
        xor = 0
        for j in range(1, n + 1):
            if j & pos:
                xor ^= int(bits[j - 1])
        if xor:
            error_pos += pos

    if error_pos != 0 and error_pos <= n: #Error de un bit
        bits[error_pos - 1] = '1' if bits[error_pos - 1] == '0' else '0'

     # Volver a poner el orden correcto
    bits.reverse()
    mensaje_corregido = ''.join(bits)

    # Verificar el bit de paridad
    paridad_calculada = sum(int(b) for b in mensaje_corregido) % 2
    if paridad_calculada != bit_extra_recibido:
        advertencia = "Hay 2 o más errores: no se pueden corregir"
    else:
        if error_pos == 0:
            advertencia = "No hay errores"
        else:
            advertencia = f"Se corrigió un error en la posición {error_pos}"

    return mensaje_corregido, advertencia

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

        temp = ""

    return "1" in result


def extraer_datos(mensaje_corregido: str):
  
    longitud_sin_extra = len(mensaje_corregido) - 1

    datos = []
    for i in range(1, longitud_sin_extra + 1):  
        if (i & (i - 1)) != 0: 
            datos.append(mensaje_corregido[i - 1])  
    return ''.join(datos)


def mostrar_mensaje(bits: str):
    return chr(int(bits,2))
    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 9998))
    print("Escuchando solicitudes ...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Se estableció conexión! ")
        while True: 
            data = conn.recv(1024).decode()
            
            if not data:
                break
            print(f"Mensaje recibido ")

            if data[0] == "0": #0 para Hamming 
                mensaje_corregido, advertencia = detectar_y_corregir(data[1:])
                if advertencia == "No hay errores":
                    print(f"Mensaje original: {extraer_datos(mensaje_corregido)}")
                    print("El mensaje era:", mostrar_mensaje(extraer_datos(mensaje_corregido)))
                    conn.sendall(b"OK\n")
                else:
                    print(advertencia)
                    conn.sendall(b"ERR\n")

            else: #1 para CRC
                print(f"Mensaje recibido: {data}")
                if(detectar_errores_CRC(data[1:])):
                    print("Se detectaron errores en el mensaje :(")
                    conn.sendall(b"ERR\n")

                else: 
                    print("No hubo un error en el mensaje :)")
                    print(f"El mensaje original es: {mostrar_mensaje(data[1:-3])} ")
                    conn.sendall(b"OK\n")







