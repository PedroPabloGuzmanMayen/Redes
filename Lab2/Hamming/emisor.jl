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

function main()
    println("prueba 1:")
    cod1 = hamming_emisor("1010")
    
    println("\nprueba 2:")
    cod2 = hamming_emisor("110011")
    
    println("\nprueba 3:")
    cod3 = hamming_emisor("1001101")
    
end

main()
