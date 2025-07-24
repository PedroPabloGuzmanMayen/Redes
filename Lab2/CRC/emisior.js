let polinomio = "1001" //Usaremos x^3 + 1

const codificarMensaje = (mensaje) => {
    let ha_Terminado = false
    let resultado = mensaje + "000"
    let operacion
    while (!ha_Terminado){
        let temp = ""
        for (let i = 0; i< polinomio.length; i++){
            operacion = parseInt(resultado[i]) ^ parseInt(polinomio[i])
            temp += operacion.toString()
        }

        if (temp[0] == "0"){
            temp = temp.slice(1)
        }
        resultado = temp + "0".repeat(resultado.length - polinomio.length)
        console.log("Resultado: " + resultado)
        resultado.length < polinomio.length ? ha_Terminado = true : ha_Terminado = false
        
        
    }
    return mensaje + resultado
    

}

console.log(codificarMensaje("0110"))



