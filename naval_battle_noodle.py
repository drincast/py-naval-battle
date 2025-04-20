class Ship:
    def __init__(self, name, size):
        self.name       = name
        self.hits       = 0
        self.positions  = []
        self.size       = size


    def place_ship(self, start_row, start_col, direction, board):
        try:
            response = True

            #Crear funcion para validar que la posicion de la nave es valida en el tablero
            if board[start_row][start_col] != "":
                response = False
            else:
                #horizontal
                if direction == 'H':
                    for i in  range(self.size):
                        
                        if board[start_row][start_col+i] != "":
                            response = False
                            break

                        board[start_row][start_row+i] = '1'
                elif direction == 'V':
                    for i in  range(self.size):
                        
                        if board[start_row+i][start_col] != "":
                            response = False
                            break

                        board[start_row+i][start_row] = '1'
                else:
                    raise Exception("La dirección no es valida", direction)
            

            return response
        except Exception as ex:
            print(ex)

    def hit(self):
        try:
            response = False
            if self.size == self.hits:
                response = True
            
            return response
        except Exception as ex:
            print(ex)

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)

class Player:
    def __init__(self, name):
        try:
            self.board = [["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]
                          , ["", "", "", "", "", "", "", "", "", ""]]
            self.name = name
            self.ships = []
            self.hips = []
        except Exception as ex:
            print(ex)

    def place_ships(self):
        try:
            row = None
            column = None
            direction = None

            destroyer = Destroyer()
            submarine = Submarine()
            battleship = Battleship()

            position_is_correct = False

            ships = [destroyer, submarine, battleship]

            #Se debe crear una forma para que cuando la posicion de la nave no es valido
            #la solicite nuevamente

            for ship in ships:

                while position_is_correct:
                    row = input(f"En que fila quires poner el {destroyer.name}")
                    column = input(f"En que columna quires poner el {destroyer.name}")
                    direction = input(f"En que dirección quires poner el {destroyer.name}")
                    position_is_correct = ship.place_ship(row, column, direction, self.board)

                    if not position_is_correct:
                        print("No se puede ubicar la nave, intenta de nuevo \n")

            
        except Exception as ex:
            print(ex)

    def print_board(self):
        try:
            for row in self.board:
                print(row)                
        except Exception as ex:
            print(ex)

    def attack(self):
        try:
            position_x = input("Indica la fila de ataque")
            position_y = input("Indica la columna de ataque")
        except Exception as ex:
            print(ex)
    