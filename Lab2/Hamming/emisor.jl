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
	return mensaje_texto = readline()
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

function calcular_integridad(lista_binarios::Vector{String})::String
    codificados = String[]
    for binario in lista_binarios
        push!(codificados, hamming_emisor(binario))
    end
    return join(codificados)
end


# Por el momento solo cambia un bit, pero se puede cambiar al aumentar el valor de count en 'trama_ruidosa'
function aplicar_ruido(trama::String)::String
    n = length(trama)
    i = rand(1:n)
    flip = trama[i] == '0' ? '1' : '0' # Verificar valor del bit en la posicion 'i'
    trama_ruidosa = String(trama)
    trama_ruidosa = replace(trama_ruidosa, trama[i] => flip; count=1)
    #println("Bit modificado en posición $i: $trama_ruidosa")
    return trama_ruidosa
end

function main()
    mensaje_texto = solicitar_mensaje()
    @assert isa(mensaje_texto, String) "Error: mensaje debe ser String"
    println("[Aplicación] Mensaje original: $mensaje_texto")

    lista_binarios = codificar_mensaje(mensaje_texto)
    @assert isa(lista_binarios, Vector{String}) "Error: codificar_mensaje debe retornar Vector{String}"
    println("[Presentación] Codificación verificada. Total letras: $(length(lista_binarios))")

    trama = calcular_integridad(lista_binarios)
    @assert isa(trama, String) "Error: calcular_integridad debe retornar String"
    println("[Enlace] Trama con redundancia: $trama")

    trama_ruidosa = aplicar_ruido(trama)
    println("[Ruido] Trama final enviada: $trama_ruidosa")
end

main()
