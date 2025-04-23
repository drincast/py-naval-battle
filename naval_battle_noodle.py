# -----------------------------------------------------------------------------
# Proyecto: py-naval-battle
# Archivo: naval_battle_noodle.py
# Descripción: Código del juego, inicialmente este archi tendra el código en espagueti
#   luego, se mejorara dividiendolo en archivos, este archivo se mantendra
# Autor: drincastX
# Licencia: MIT License (o la licencia que hayas usado)
# Fecha creación: 2025-04-19
# -----------------------------------------------------------------------------
# Modificacion
# Autor: drincastX
# Fecha: 2025-04-20
# Descripción: se continua con la codificación, se probo, se debe agregar la identificación de nave hundida,
#       mejorar la interacción con el usuario.
# -----------------------------------------------------------------------------

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Ship:
    def __init__(self, code, name, size, type):
        self.code       = code
        self.name       = name
        self.hits       = 0
        self.positions  = []        
        self.size       = size
        self.type       = type


    def add_positions(self, row, col):
        self.positions.append((row, col))

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

                        board[start_row][start_col+i] = self.code
                        self.add_positions(start_row, start_col+i)
                elif direction == 'V':
                    for i in  range(self.size):
                        
                        if board[start_row+i][start_col] != "":
                            response = False
                            break

                        board[start_row+i][start_col] = self.code
                        self.add_positions(start_row+i, start_col)
                else:
                    raise Exception("La dirección no es valida (H o V)", direction)            

            return response
        except Exception as ex:
            raise ex
            # print(ex)
            # logger.exception("Ocurrió una excepción")

    def hit(self):
        try:
            response = False
            self.hits += 1
            if self.size == self.hits:
                response = True
            
            return response
        except Exception as ex:
            print(ex)

class Destroyer(Ship):
    def __init__(self):
        super().__init__('D', 'Destructor', 2, 'D')

class Submarine(Ship):
    def __init__(self):
        super().__init__('S', 'Submarino', 3, 'S')

class Battleship(Ship):
    def __init__(self):
        super().__init__('B', 'Acorazado', 4, 'B')

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
            self.hits_board = [[' ' for _ in range(10)] for _ in range(10)]
        except Exception as ex:
            print(ex)

    def all_ships_sunk(self):
        ship_sank = None
        all_ships_sunk = []
        response = False

        try:
            count_ships = len(self.ships)

            if count_ships == 0:
                response = True

            # for ship in self.ships:
            #     if len(ship.positions) == 0:
            #         break

            #     if ship.positions[2] == "H":
            #         for i in range(ship.size):
            #                 if self.board[ship.positions[0]][ship.positions[1] + i] == 'X':
            #                     ship_sank = True
            #                 else:
            #                     ship_sank = False
            #                     break                    
            #         else:
            #             for i in range(ship.size):
            #                 if self.board[ship.positions[0] + i][ship.positions[1]] == 'X':
            #                     ship_sank = True
            #                 else:
            #                     ship_sank = False
            #                     break
                
            #     if ship_sank:
            #         all_ships_sunk.append(ship)

            # if len(self.ships) == len(all_ships_sunk):
            #     response = True
        except Exception as ex:
            raise ex

        return response

    def place_ships(self):
        try:
            row = None
            column = None
            direction = None

            destroyer = Destroyer()
            submarine = Submarine()
            battleship = Battleship()

            position_is_correct = False
            self.ships = [destroyer, submarine, battleship]

            #TODO: Se debe crear una forma para que cuando la posicion de la nave no es valido
            #la solicite nuevamente, probar ya se agreo un ciclo while para hacerlo

            print(len(self.ships))
            print(f"\nUbica tus naves {self.name}")

            for ship in self.ships:
                print(ship, position_is_correct)
                while not position_is_correct:
                    row = int(input(f"En que fila quires poner el {ship.name}: ")) - 1
                    column = int(input(f"En que columna quires poner el {ship.name}: ")) - 1
                    direction = input(f"En que dirección quires poner el {ship.name}: ").upper()
                    position_is_correct = ship.place_ship(row, column, direction, self.board)

                    if not position_is_correct:
                        print("No se puede ubicar la nave, intenta de nuevo \n")                        

                position_is_correct = False
                self.print_board('board')

            print("Se ubicaron todas las naves")
            self.print_board('board')
            
        except Exception as ex:
            print(ex)
            logger.exception("Ocurrió una excepción")

    def print_board(self, which):
        try:
            whith_board = self.board if which == 'board' else self.hits_board

            for row in whith_board:
                row2 = [x if x!= '' else ' ' for x in row ]
                # print(row if row != '' else ' ') 
                print(row2)               
        except Exception as ex:
            print(ex)

    def attack(self, enemy):
        try:
            ship_sank = None

            position_x = int(input("\nIndica la fila de ataque: ")) - 1
            position_y = int(input("Indica la columna de ataque: ")) - 1

            print("\n", len(enemy.board), position_x, position_y, enemy.board)

            if enemy.board[position_x][position_y] != "":
                ship_code = enemy.board[position_x][position_y]
                if self.hits_board[position_x][position_y] == "X" \
                    or self.hits_board[position_x][position_y] == "-":
                    
                    print("Ya habías disparado a esta área")
                else:
                    print("En el blanco !!!")
                    ship_code = enemy.board[position_x][position_y]
                    enemy.board[position_x][position_y] = "X"
                    self.hits_board[position_x][position_y] = "X"
                    #Validar si se hundio el barco
                    ship_sank = self.validate_ship_sank(ship_code, position_x, position_y, enemy)

                    if ship_sank != None:
                        print("Nave destruida !!!!")
                        enemy.ships.remove(ship_sank)                    
            else:
                print("Impacto en el agua")
                enemy.board[position_x][position_y] = "-"
                self.hits_board[position_x][position_y] = "-"

        except Exception as ex:
            print(ex)
            logger.exception("Ocurrió una excepción")
    
    def validate_ship_sank(self, ship_code, position_x, position_y, enemy):
        try:
            ship_sank = None
            ship_enemy_sank = None

            for ship in enemy.ships:
                if ship_code == ship.code:
                    ship_sank = ship.hit()


                # if ship.position[2] == "H":
                #     for i in range(ship.size):
                #         if enemy.board[position_x][position_y + i] == 'X':
                #             ship_sank = True
                #         else:
                #             ship_sank = False
                #             break
                # else:
                #     for i in range(ship.size):
                #         if enemy.board[position_x + i][position_y] == 'X':
                #             ship_sank = True
                #         else:
                #             ship_sank = False
                #             break

                    if ship_sank == False:
                        break
                    else:
                        ship_enemy_sank = ship
            
            return ship_enemy_sank
        except Exception as ex:
            print(ex)

class BattleshipGame:
    def __init__(self):
        try:
            self.player1 = Player('Jugador 1')
            self.player2 = Player('Jugador 2')
        except Exception as ex:
            print(ex)

    def play(self):
        end_game = False
        player1_win = False
        player2_win = False

        try:
            self.player1.place_ships()
            self.player2.place_ships()

            while not end_game:
                self.player1.attack(self.player2)
                print("playe1 fin turno")
                player1_win = self.player2.all_ships_sunk()

                if(player1_win):
                    break

                self.player2.attack(self.player1)
                player2_win = self.player1.all_ships_sunk()

                if(player2_win):
                    break

            if player1_win:
                print(f"El jugador {self.player1.name} ha ganado !!!!")
            else:
                print(f"El jugador {self.player2.name} ha ganado !!!!")
        except Exception as ex:
            print(ex)
            logger.exception("Ocurrió una excepción")

game = BattleshipGame()
game.play()