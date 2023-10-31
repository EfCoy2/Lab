
def contar_vocales(cadena):
    cadena = cadena.lower()
    contador = 0
    vocales = "aeiou"
    for letra in cadena:
        if letra in vocales:
            contador+=1
    return contador
cadena = "Murcielago"
cantidad_vocales = contar_vocales(cadena)
print(cantidad_vocales)