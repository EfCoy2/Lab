while True:
  print("Menù:")
  print("1. Factorial")
  print("2. Secuencia de Fibonacci")
  print("3. Salir")
  opcion=int(input("No. de la opciòn: "))
  if opcion==1:
    x=int(input("Ingrese un nùmero: "))
    factorial=1
    i=1
    y=1
    while(i<=x):
      factorial=factorial*i
      i=i+1
    print(str(x)+"="+str(x)+"*")
    print(list(range(y,x)))
    print("="+str(factorial))
    print("")
  elif opcion==2:
    x=int(input("¿Cuantos nùmeros? "))
    n1, n2=0, 1
    c=0
    if x<=0:
      print("Entrar un valore vàlido")
      print("")
    elif x==1:
      print("Fibonacci de"+str(x)+":")
      print(n1)
    else:
      print("Secuencia Fibonacci:")
      while c<x:
        print(n1)
        nth=n1+n2

        n1=n2
        n2=nth
        c+=1
        
  elif opcion==3:
    print("Saliendo. . . ")
    break
  else:
    print("Eliga una opciòn correcta")
    print("")

