while True:
    class Persona:
      #Constructor que inicializa los datos de la persona
      def __init__(self):
          self.nombres = ""
          self.apellidos = ""
          self.apellido_casada = ""
          self.fecha_nacimiento = ""
        #Metodo 1, define los nombres
      def insertar_nombres(self, nombres):
          self.nombres = nombres
        #Metodo 2, define los apellidos
      def insertar_apellidos(self, apellidos):
          self.apellidos = apellidos
        #Metodo 3, define el apellido de casada
      def insertar_apellido_casada(self, apellido_casada):
          self.apellido_casada = apellido_casada
        #Metodo 4, define la fecha de nacimiento
      def insertar_fecha_nacimiento(self, fecha_nacimiento):
          self.fecha_nacimiento = fecha_nacimiento
          #obtiene nombres
      def obtener_nombres(self):
          return self.nombres
      #obtiene ambos tipos de apellidos si es que tiene de casada
      def obtener_apellidos(self):
          if self.apellido_casada:
              return f"{self.apellidos}, de casada {self.apellido_casada}"
          return self.apellidos
      #obtiene el conjunto de nombres y los tipos de apellidos
      def obtener_nombre_completo(self):
          return f"{self.nombres} {self.obtener_apellidos()}"
      #obtiene la fecha de nacimiento
      def obtener_fecha_nacimiento(self):
          return self.fecha_nacimiento

#Solicita los datos   
    persona = Persona()
    persona.insertar_nombres(input("Ingrese sus nombres: "))
    persona.insertar_apellidos(input("Ingrese sus apellidos: "))
    apellido_casada = input("Si tiene ingrese su apellido de casada, si no tiene no ingrese nada: ")
    if apellido_casada:
         persona.insertar_apellido_casada(apellido_casada)
    persona.insertar_fecha_nacimiento(input("Ingrese su fecha de nacimiento: "))

#Imprime lo solicitado, la fecha de nacimiento no aparecia que se debia agregar pero por si acaso lo agregue
    print("Nombre completo: ", persona.obtener_nombre_completo())
    print("Fecha de nacimiento: ", persona.obtener_fecha_nacimiento())
    print("")