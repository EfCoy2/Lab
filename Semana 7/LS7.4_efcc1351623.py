print("ejercicio 4: Jerarquía de operaciones")
print("Eliga la operación a realizar")
print("1. a*b+c")
print("2. a*(b+c)")
print("3. a/(b*c)")
print("4. (3a+2b)/(c**2)")
print("5. Fórmula cuadratica")
print("6. Salir")

e=int(input("No. de operación: "))
if e==6:
    print("Saliendo. . .")
if 0<e<6:
    a=int(input("Ingrese el valor de la variable a: "))
    b=int(input("Ingrese el valor de la variable b: "))
    c=int(input("Ingrese el valor de la variable c: "))
    i=(b**2)-4*a*c
    uno=a*b+c
    dos=a*(b+c)
    tres=a/(b*c)
    cuatro=(3*a+2*b)/c**2
    if e==1:
        print("Resultado: "+str(uno))
    if e==2:
        print("Resultado: "+str(dos))
    if e==3:
        print("Resultado: "+str(tres))
    if e==4:
        print("Resultado: "+str(cuatro))
    if e==5 and a==0:
        print("")
        print("Error, la variable a no puede ser 0")
        print("")
    if e==5 and i<0:
        print("")
        print("Error, número imaginario")
        print("")
    if e==5 and a!=0 and i>=0:
        ii=-b+(i**0.5)
        iii=ii/(2*a)
        iv=-b-(i**0.5)
        v=iv/(2*a)
        print("Valor 1: "+str(iii))
        print("Valor 2: "+str(v))
        print("")

if e!=6:
   print("¿Que quiere? 1.Regresar al menú, 2.Salir")
   m=int(input("No. de la opción: "))
   while m==2:
     break
   while m==1:
      print("Eliga la operación a realizar")
      print("1. a*b+c")
      print("2. a*(b+c)")
      print("3. a/(b*c)")
      print("4. (3a+2b)/(c**2)")
      print("5. Fórmula cuadratica")
      print("6. Salir")
      e=int(input("No. de operación: "))
      if e==6:
        print("Saliendo. . .")
      if 0<e<6:
         a=int(input("Ingrese el valor de la variable a: "))
         b=int(input("Ingrese el valor de la variable b: "))
         c=int(input("Ingrese el valor de la variable c: "))
         i=(b**2)-4*a*c
         uno=a*b+c
         dos=a*(b+c)
         tres=a/(b*c)
         cuatro=(3*a+2*b)/c**2
         if e==1:
            print("Resultado: "+str(uno))
         if e==2:
            print("Resultado: "+str(dos))
         if e==3:
            print("Resultado: "+str(tres))
         if e==4:
            print("Resultado: "+str(cuatro))
         if e==5 and a==0:
            print("")
            print("Error, la variable a no puede ser 0")
            print("")
         if e==5 and i<0:
            print("")
            print("Error, número imaginario")
            print("")
         if e==5 and a!=0 and i>=0:
            ii=-b+(i**0.5)
            iii=ii/(2*a)
            iv=-b-(i**0.5)
            v=iv/(2*a)
            print("Valor 1: "+str(iii))
            print("Valor 2: "+str(v))
            print("")
         if e==1 or e==2 or e==3 or e==4 or e==5:
            print("¿Que quiere? 1.Regresar al menú, 2.Salir")
            n=int(input("No. de la opción: "))
            while n==2:
               break
