
#las variables creadas para almacenar cada tipo de caracter, empiezan en 0 ya que inicialmente no se sabe su valor pero esto cambiara en el ciclo
cadena_de_caracteres = input("Ingrese la cadena de codigo: ")
numero_de_ceros = 0
numero_de_unos = 0
numero_de_otros_caracteres = 0


for caracter in cadena_de_caracteres:
    #Compara si el caracter es igual a 0 y le agrega a la cuenta de ceros hasta que ya no existan mas ceros
    if caracter == "0":
        numero_de_ceros += 1
        continue
#Compara si el caracter es igual a 1 y le agrega a la cuenta de unos hasta que ya no existan mas unos
    if caracter == "1":
        numero_de_unos += 1
        continue
#Cuando los anteriores bloques no sean verdaderos este analiza los otros tipos de caracteres y los agrega a su propia cuenta
    numero_de_otros_caracteres += 1

#imprime los valores
print("Numero de ceros: "+str(numero_de_ceros))
print("Numero de unos: "+str(numero_de_unos))
print("Otros caracteres: "+str(numero_de_otros_caracteres))
