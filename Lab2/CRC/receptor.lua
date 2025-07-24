local polinomio = "1001"  -- x^3 + 1

-- XOR entre dos cadenas binarias del mismo largo
function xor_cadenas(a, b)
    local resultado = ""
    for i = 1, #a do
        local bit_a = tonumber(string.sub(a, i, i))
        local bit_b = tonumber(string.sub(b, i, i))
        local xor = bit_a ~ bit_b
        resultado = resultado .. tostring(xor)
    end
    return resultado
end

-- Verifica si un mensaje recibido es válido (sin errores)
function verificar_crc(mensaje_codificado)
    local n = #polinomio
    local resto = string.sub(mensaje_codificado, 1, n)
    local indice = n + 1

    while indice <= #mensaje_codificado + 1 do
        if string.sub(resto, 1, 1) == "1" then
            resto = xor_cadenas(resto, polinomio)
        else
            resto = xor_cadenas(resto, string.rep("0", n))
        end

        resto = string.sub(resto, 2)
        if indice <= #mensaje_codificado then
            resto = resto .. string.sub(mensaje_codificado, indice, indice)
        end
        indice = indice + 1
    end

    print("Residuo final:", resto)

    if resto == string.rep("0", n - 1) then
        print("Mensaje válido: no hay errores")
        return true
    else
        print("Errores detectados en el mensaje")
        return false
    end
end

-- Prueba
verificar_crc("0110100") 



