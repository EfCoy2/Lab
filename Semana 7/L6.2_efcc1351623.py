print("ejercicio 2: operaciones aritmèticas")

a = int(input("Ingrese un nùmero: "))
b = int(input("Ingrese un  segundo nùmer: "))

c = a+b
d= a-b
e = a*b
f = a/b
g = a%b
h = a//b
i = a**b

print ("Eliga una operaciòn")
print ("Operacines: 1-Suma, 2-Resta, 3-Multiplicaciòn, 4-Divisiòn, 5-Mòdulo, 6-Cociente, 7-Exponencial y 8- Salir")
j=int(input("Nùmero de la operaciòn: "))
print("")

if j == 1:
     print("Resultado:")
     print(c)
if j == 2:
     print("Resultado:")
     print(d)
if j == 3:
     print("Resultado:")
     print(e)
if j == 4:
     print("Resultado:")
     print(f)
if j == 5:
     print("Resultado:")
     print(g)
if j == 6:
     print("Resultado:")
     print(h)
if j ==7:
     print("Resultado:")
     print(i)
if j >= 9:
     print("Error")
print("")
while j!=8:
     print ("Eliga una operaciòn")
     print ("Operacines: 1-Suma, 2-Resta, 3-Multiplicaciòn, 4-Divisiòn, 5-Mòdulo, 6-Cociente, 7-Exponencial y 8- Salir")
     j=int(input("Nùmero de la operaciòn: "))
     print("")
     if j == 1:
          print("Resultado:")
          print(c)
     if j == 2:
          print("Resultado:")
          print(d)
     if j == 3:
          print("Resultado:")
          print(e)
     if j == 4:
          print("Resultado:")
          print(f)
     if j == 5:
          print("Resultado:")
          print(g)
     if j == 6:
          print("Resultado:")
          print(h)
     if j ==7:
          print("Resultado:")
          print(i)
     if j >= 9:
          print("Error")
     print("")

while j == 8:
     print("Saliendo...")
     break
