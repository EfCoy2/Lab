print("ejercicio 3: Jerarquía de operaciones")
a=int(input("Ingrese el valor de la variable a: "))
b=int(input("Ingrese el valor de la variable b: "))
c=int(input("Ingrese el valor de la variable c: "))

uno=a*b+c
dos=a*(b+c)
tres=a/(b*c)
cuatro=(3*a+2*b)/c**2

print("Valor a*b+c: "+str(uno))
print("Valor a*(b+c): "+str(dos))
print("Valor a/(b*c): "+str(tres))
print("Valor (3a+2b)/(c**2)): "+str(cuatro))