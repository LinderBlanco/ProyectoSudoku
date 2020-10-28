class Solution:
    def desencriptar(self, clave, mensajeAEnviarEncriptado):
        mensajeDesencriptado = ""
        cadenaAleatoria=""

        cadena=mensajeAEnviarEncriptado[:80]
        for i in range(0,len(cadena),8):
            cadenaAleatoria+=str(int(cadena[i:i+8],2))

        mensajeCodificado=str(mensajeAEnviarEncriptado[80:])

        MAX_LENGTH = 256
        cadenaDeInicio = ""
        isKey = True
        while (len(cadenaDeInicio) < MAX_LENGTH):
            cadenaDeInicio += clave if isKey else str(cadenaAleatoria)
            isKey = not isKey
        cadenaDeInicio=cadenaDeInicio[0:MAX_LENGTH]


        arr = [i for i in range(MAX_LENGTH)]
        for i in range(MAX_LENGTH):
            j = int(cadenaDeInicio[i])
            arr[i], arr[(i + j) % MAX_LENGTH] = arr[(i + j) % MAX_LENGTH], arr[i]
        mensajeDesencriptado=arr

        # Procedemos a hallar la lista de numeros a Binario
        listaABinario = ""
        for numero in arr:
            listaABinario += format(numero, '08b')

        arraydelBinario = listaABinario[:len(mensajeCodificado)]



        mensajeBinario = ""
        for j in range(len(mensajeCodificado)):
            mensajeBinario += '0' if mensajeCodificado[j] == arraydelBinario[j] else '1'



        mensajeADecimal=""

        cadena2=mensajeBinario[:]
        for i in range(0,len(cadena2),8):
            mensajeADecimal+=str(chr(int(int(cadena2[i:i+8],2))))
                

        mensajeDesencriptado=mensajeADecimal

        return mensajeDesencriptado


clave="9876543210"
mensajeAEnviarEncriptado="00001001000001110000000100001000000010010000010000000010000000010000000100000101010001000100010111011011101110000101011010101111010100011011111101001001001010000101111101011101010111100011010101011111010001010100011001010010010111010101110101001110"
print(Solution().desencriptar(clave,mensajeAEnviarEncriptado))
