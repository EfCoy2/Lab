class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Ship:
    def __init__(self, length):
        self.length = length
        self.coordinates = []

    def place_ship(self, start_coord, direction):
        self.coordinates = [start_coord]
        for i in range(1, self.length):
            if direction == 'horizontal':
                new_coord = Coordinate(start_coord.x + i, start_coord.y)
            else:
                new_coord = Coordinate(start_coord.x, start_coord.y + i)
            self.coordinates.append(new_coord)

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

    def is_valid_location(self, coord):
        return 0 <= coord.x < self.size and 0 <= coord.y < self.size

    def place_ship(self, ship, start_coord, direction):
        if not self.is_valid_location(start_coord):
            return False

        for coord in ship.coordinates:
            if not self.is_valid_location(coord) or self.grid[coord.x][coord.y] != ' ':
                return False

        for coord in ship.coordinates:
            self.grid[coord.x][coord.y] = 'S'
        self.ships.append(ship)
        return True

class Turn:
    def __init(self, player):
        self.player = player

class BattleshipGame:
    def __init__(self, board_size, ship_lengths):
        self.board = Board(board_size)
        self.ships = []

        for length in ship_lengths:
            ship = Ship(length)
            self.ships.append(ship)

        self.board.print_board()

    def play(self):
        print("Coloque sus 5 barcos en el tablero.")
        for ship in self.ships:
            while True:
                try:
                    start_x = int(input("Ingrese la coordenada x de inicio: "))
                    start_y = int(input("Ingrese la coordenada y de inicio: "))
                    direction = input("Ingrese la dirección (horizontal o vertical): ").lower()

                    start_coord = Coordinate(start_x, start_y)
                    ship.place_ship(start_coord, direction)

                    if self.board.place_ship(ship, start_coord, direction):
                        print("Barco colocado con éxito.")
                        self.board.print_board()
                        break
                    else:
                        print("Ubicación inválida para el barco. Inténtelo de nuevo.")
                except ValueError:
                    print("Por favor, ingrese coordenadas válidas.")

def main():
    board_size = 10
    ship_lengths = [5, 5, 3, 3, 3]

    print("Proyecto 2")
    print("El tablero tiene un tamaño de {}x{}.".format(board_size, board_size))
    game = BattleshipGame(board_size, ship_lengths)
    game.play()

if __name__ == "__main__":
    main()
