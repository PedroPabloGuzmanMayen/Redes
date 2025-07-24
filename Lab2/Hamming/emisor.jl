function calcular_r(m::Int)
	r=0
	while m + r + 1 > 2^r
		r+=1
	end
	return r
end

function insertar_bits_paridad(bits::Vector{Char}, r::Int)
	for i in 1:r
		insert!(bits, 2^(i-1), '0')
	end
	return bits
end

function calcular_bits_paridad(bits::Vector{Char}, r::Int)
	n = length(bits)
	for i in 1:r
		pos = 2^(i-1)
		paridad=0
		for j in 1:n
			if j & pos != 0
				bit = parse(Int, bits[j])
				paridad = xor(paridad, bit)
			end
		end
		bits[pos] = Char(paridad + 0x30)
	end
	return bits
end

# Main del emisor
function hamming_emisor(mensaje::String)::String
    println("Mensaje original: $mensaje")

    m = length(mensaje)
    r = calcular_r(m)
    println("Número de bits de paridad necesarios: $r")

    bits = collect(mensaje)
    bits = insertar_bits_paridad(bits, r)
    println("Bits con espacios de paridad: ", join(bits))

    bits = calcular_bits_paridad(bits, r)
    mensaje_codificado = join(bits)
    println("Mensaje codificado con Hamming: $mensaje_codificado")
    return mensaje_codificado
end

# main para pruebas para la parte 1 del lab
function main()
	println("PRUEBA 1") 
    hamming_emisor("1010")

	println("\nPRUEBA 2")
    hamming_emisor("110011")

    println("\nPRUEBA 3 ")
    hamming_emisor("1001101")
end

main()
