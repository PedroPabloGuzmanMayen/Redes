using Random

function calcular_r(m::Int)
    r = 0
    while m + r + 1 > 2^r
        r += 1
    end
    return r
end

function hamming_emisor(mensaje::String)::String
    println("Mensaje original: $mensaje")
    m = length(mensaje)
    r = calcular_r(m)
    println("Bits de paridad necesarios: $r")

    n = m + r
    bits = Vector{Char}(undef, n)
    fill!(bits, '0')

    mensaje_idx = 1
    for i in 1:n
        if !es_potencia_de_2(i)
            bits[i] = mensaje[mensaje_idx]
            mensaje_idx += 1
        end
    end

    println("Bits con espacios de paridad: ", join(bits))

    for i in 1:r
        pos_paridad = 2^(i-1)
        paridad = 0

        for j in 1:n
            if (j & pos_paridad) != 0
                bit_val = parse(Int, bits[j])
                paridad = xor(paridad, bit_val)
            end
        end

        bits[pos_paridad] = Char(paridad + 0x30)
    end

    mensaje_codificado = join(bits)
    println("Mensaje codificado: $mensaje_codificado")
    return mensaje_codificado
end

function es_potencia_de_2(n::Int)::Bool
    return n > 0 && (n & (n - 1)) == 0
end

function solicitar_mensaje()
    println("ingrese el mensaje a enviar: ")
    mensaje_texto = readline()

    println("ingrese cantidad de bits de ruido a insertar (0 para ninguno): ")
    ruido = parse(Int, readline())

    return mensaje_texto, ruido
end

function codificar_mensaje(mensaje_texto::String)::Vector{String}
    binarios = String[]
    for c in mensaje_texto
        ascii = UInt8(c)
        push!(binarios, bitstring(ascii))  # 8 bits por carácter
    end
    println("ASCII binario por letra: ", join(binarios, " "))
    return binarios
end

function calcular_integridad(lista_binarios::Vector{String})::Vector{String}
    codificados = String[]
    for binario in lista_binarios
        push!(codificados, hamming_emisor(binario))
    end
    return codificados
end

function aplicar_ruido(trama_codificada::Vector{String}, tasa::Int)::Vector{String}
    prob = tasa / 100  # Probabilidad de flip por bit
    trama_con_ruido = copy(trama_codificada)

    for i in eachindex(trama_con_ruido)
        bloque = trama_con_ruido[i]
        nuevo_bloque = Vector{Char}(bloque)

        for j in eachindex(nuevo_bloque)
            if rand() < prob
                nuevo_bloque[j] = nuevo_bloque[j] == '0' ? '1' : '0'
            end
        end

        trama_con_ruido[i] = join(nuevo_bloque)
    end

    return trama_con_ruido
end

function main()
    mensaje_texto, ruido = solicitar_mensaje()
    @assert isa(mensaje_texto, String) "Error: mensaje debe ser String"
    println("[Aplicación] Mensaje original: $mensaje_texto")

    lista_binarios = codificar_mensaje(mensaje_texto)
    @assert isa(lista_binarios, Vector{String}) "Error: codificar_mensaje debe retornar Vector{String}"
    println("[Presentación] Codificación verificada. Total letras: $(length(lista_binarios))")

    codificados = calcular_integridad(lista_binarios)
    trama = join(codificados, " ")
    println("[Enlace] Trama con redundancia: $trama")

    trama_con_ruido = aplicar_ruido(copy(codificados), ruido)
    trama_final = join(trama_con_ruido, " ")
    println("[Ruido] Trama final enviada: $trama_final")
end

main()
