class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# La clase Coordenada se utiliza para representar las coordenadas (x, y) en el tablero.

class Barco:
    def __init__(self, longitud):
        self.longitud = longitud
        self.coordenadas = []

    def colocar_barco(self, coordenada_inicial, direccion):
        self.coordenadas = [coordenada_inicial]
        for i in range(1, self.longitud):
            if direccion == 'horizontal':
                nueva_coordenada = Coordenada(coordenada_inicial.x + i, coordenada_inicial.y)
            else:
                nueva_coordenada = Coordenada(coordenada_inicial.x, coordenada_inicial.y + i)
            self.coordenadas.append(nueva_coordenada)

# La clase Barco se utiliza para representar los barcos con una longitud específica y sus ubicaciones en el tablero.

class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.grid = [[' ' for _ in range(tamaño)] for _ in range(tamaño)]
        self.barcos = []

    def mostrar_tablero(self):
        for fila in self.grid:
            print(" ".join(fila))

    def es_ubicacion_valida(self, coordenada):
        return 0 <= coordenada.x < self.tamaño and 0 <= coordenada.y < self.tamaño

    def colocar_barco(self, barco, coordenada_inicial, direccion):
        if not self.es_ubicacion_valida(coordenada_inicial):
            return False

        for coordenada in barco.coordenadas:
            if not self.es_ubicacion_valida(coordenada) or self.grid[coordenada.y][coordenada.x] != ' ':
                return False

        for coordenada in barco.coordenadas:
            self.grid[coordenada.y][coordenada.x] = 'S'
        self.barcos.append(barco)
        return True

    def es_todos_los_barcos_hundidos(self):
        return all(barco.esta_hundido() for barco in self.barcos)

# La clase Tablero se utiliza para representar el tablero de juego y lleva un registro de las ubicaciones de los barcos.

class Turno:
    def __init(self, jugador):
        self.jugador = jugador

# La clase Turno se utiliza para representar los turnos de los jugadores.

class JuegoBattleship:
    def __init__(self, tamaño_tablero, longitudes_de_barcos):
        self.tablero = Tablero(tamaño_tablero)
        self.barcos = []

        for longitud in longitudes_de_barcos:
            barco = Barco(longitud)
            self.barcos.append(barco)

        self.tablero.mostrar_tablero()

    def jugar(self):
        print("Coloque sus 5 barcos en el tablero.")
        for barco in self.barcos:
            while True:
                try:
                    coordenada_inicial_x = int(input("Ingrese la coordenada x de inicio: "))
                    coordenada_inicial_y = int(input("Ingrese la coordenada y de inicio: "))
                    direccion = input("Ingrese la dirección (horizontal o vertical): ").lower()

                    coordenada_inicial = Coordenada(coordenada_inicial_x, coordenada_inicial_y)
                    barco.colocar_barco(coordenada_inicial, direccion)

                    if self.tablero.colocar_barco(barco, coordenada_inicial, direccion):
                        print("Barco colocado con éxito.")
                        self.tablero.mostrar_tablero()
                        break
                    else:
                        print("Ubicación inválida para el barco. Inténtelo de nuevo.")
                except ValueError:
                    print("Por favor, ingrese coordenadas válidas.")

    def tomar_turno(self, tablero_oponente):
        print("Es su turno para adivinar la ubicación del barco de su oponente.")
        while True:
            try:
                coordenada_adivinanza_x = int(input("Ingrese la coordenada x de adivinanza: "))
                coordenada_adivinanza_y = int(input("Ingrese la coordenada y de adivinanza: "))
                coordenada_adivinanza = Coordenada(coordenada_adivinanza_x, coordenada_adivinanza_y)

                for barco in tablero_oponente.barcos:
                    if barco.is_hit(coordenada_adivinanza):
                        print("¡Has acertado!")
                        tablero_oponente.grid[coordenada_adivinanza_y][coordenada_adivinanza_x] = 'H'
                        return
                else:
                    print("Agua. Inténtelo de nuevo.")
                    tablero_oponente.grid[coordenada_adivinanza_y][coordenada_adivinanza_x] = 'M'
            except ValueError:
                print("Por favor, ingrese coordenadas válidas.")

def main():
    tamaño_tablero = 10
    longitudes_de_barcos = [5, 5, 3, 3, 3]

    print("Proyecto 2")
    print("El tablero tiene un tamaño de {}x{}.".format(tamaño_tablero, tamaño_tablero))
    print("Decida las posiciones de sus naves, primero se colocarán los mas grandes y luego se colocaran los pequeños")

    tablero_jugador = Tablero(tamaño_tablero)
    juego_jugador = JuegoBattleship(tamaño_tablero, longitudes_de_barcos)
    juego_jugador.jugar()

    tablero_oponente = Tablero(tamaño_tablero)
    juego_oponente = JuegoBattleship(tamaño_tablero, longitudes_de_barcos)
    juego_oponente.jugar()

    while True:
        juego_jugador.tomar_turno(tablero_oponente)
        tablero_jugador.mostrar_tablero()
        if tablero_oponente.es_todos_los_barcos_hundidos():
            print("¡Felicidades, has ganado!")
            break

        juego_oponente.tomar_turno(tablero_jugador)
        tablero_oponente.mostrar_tablero()
        if tablero_jugador.es_todos_los_barcos_hundidos():
            print("¡El oponente ha ganado!")
            break

if __name__ == "__main__":
    main()
