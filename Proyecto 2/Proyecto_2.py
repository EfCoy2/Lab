class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Barco:
    def __init__(self, length):
        self.length = length
        self.coordenadas = []

    def colocar_barco(self, inicio_coord, direccion):
        self.coordenadas = [inicio_coord]
        for i in range(1, self.length):
            if direccion == 'horizontal':
                nueva_coord = Coordenadas(inicio_coord.x + i, inicio_coord.y)
            else:
                nueva_coord = Coordenadas(inicio_coord.x, inicio_coord.y + i)
            self.coordenadas.append(nueva_coord)

class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.grid = [[' ' for _ in range(tamaño)] for _ in range(tamaño)]
        self.barcos = []

    def imprimir_tablero(self):
        for row in self.grid:
            print(" ".join(row))

    def valido(self, coord):
        return 0 <= coord.x < self.size and 0 <= coord.y < self.size

    def colocar_barco(self, barco, inicio_coord, direccion):
        if not self.valido(inicio_coord):
            return False

        for coord in barco.coordenadas:
            if not self.valido(coord) or self.grid[coord.x][coord.y] != ' ':
                return False

        for coord in barco.coordenadas:
            self.grid[coord.x][coord.y] = 'S'
        self.barcos.append(barco)
        return True

class Turno:
    def __init(self, player):
        self.player = player
