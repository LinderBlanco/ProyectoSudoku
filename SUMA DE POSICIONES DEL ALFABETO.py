
def posicion(letra):
    alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alfabeto.find(letra)+1

def contar(palabra):
    suma=0
    for letra in palabra.upper():
        suma+=posicion(letra)
    return suma

palabra= input("Ingrese una palabra o letra: ")
print("Su valor es:", contar(palabra))