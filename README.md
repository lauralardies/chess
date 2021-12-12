# chess

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/chess)
https://github.com/lauralardies/chess

Hemos creado un programa en el cual el usuario, al iniciar una partida de ajedrez, crea un fichero el cual debe nombrar. Una vez nombrado el fichero, la partida comienza. Primero siempre se pregunta si el usuario quiere hacer un movimiento. Si es así, el usuario debe introducir la fila y columna de la ficha que quiere mover además de la fila y columna de donde quiere desplazar la ficha seleccionada. Esto es así hasta que el usuario decida que quiere terminar la partida. Una vez terminada la partida, el usuario escoge si quiere revisar alguna jugada. Si es así, se le pide introducir el número de la jugada que quiere revisar y se imprime el tablero de la misma. Puede revisar todas las jugadas que quiera todas las veces que quiera. 


El diagrama de flujo que tenemos en nuestro código es el siguiente:

<br>
<img height="400" src="https://github.com/lauralardies/chess/blob/main/Chess.jpg" />
<br>

```
class Chess():
        board = []
        movement = 0
        board_name = ""

        def __init__(self, board_name) -> None:
                self.board_name = board_name
                self.board = [[" " for i in range(8)] for i in range(8)]
                self.chessPieces()

                f = open( self.board_name + ".txt", "w", encoding="utf8")
                for i in range(8):
                        for j in range(8):
                                f.write(self.board[i][j] + "\t")
                        f.write("\n")

                f.close

        def chessPieces(self):
                self.board[0][0] = chr(0x2656)
                self.board[0][1] = chr(0x2658)
                self.board[0][2] = chr(0x2657)
                self.board[0][3] = chr(0x2655)
                self.board[0][4] = chr(0x2654)
                self.board[0][5] = chr(0x2657)
                self.board[0][6] = chr(0x2658)
                self.board[0][7] = chr(0x2656)
                self.board[1][0] = chr(0x2659)
                self.board[1][1] = chr(0x2659)
                self.board[1][2] = chr(0x2659)
                self.board[1][3] = chr(0x2659)
                self.board[1][4] = chr(0x2659)
                self.board[1][5] = chr(0x2659)
                self.board[1][6] = chr(0x2659)
                self.board[1][7] = chr(0x2659)
                self.board[6][0] = chr(0x265F)
                self.board[6][1] = chr(0x265F)
                self.board[6][2] = chr(0x265F)
                self.board[6][3] = chr(0x265F)
                self.board[6][4] = chr(0x265F)
                self.board[6][5] = chr(0x265F)
                self.board[6][6] = chr(0x265F)
                self.board[6][7] = chr(0x265F)
                self.board[7][0] = chr(0x265C)
                self.board[7][1] = chr(0x265E)
                self.board[7][2] = chr(0x265D)
                self.board[7][3] = chr(0x265B)
                self.board[7][4] = chr(0x265A)
                self.board[7][5] = chr(0x265D)
                self.board[7][6] = chr(0x265E)
                self.board[7][7] = chr(0x265C)

        def saveBoard(self):
                f = open(self.board_name + ".txt", "a", encoding="utf8")
                for i in range(8):
                        for j in range(8):
                                f.write(self.board[i][j] + "\t")
                        f.write("\n")

                f.close

        def printBoard(self, movement):
                i = (movement - 1) * 8
                j = movement * 8 - 1

                f = open(self.board_name + ".txt", "r", encoding="utf8")
                lines = f.readlines()

                for k in range(i, j + 1):
                        print(lines[k])

        def validPlacement(self, x, y, placement):
                if x in range(8):
                        if y in range (8):
                                if placement == True:
                                        if self.board[x][y] == " ":
                                                print("There is not a piece here! Please select a row and a column in which there is a piece.")
                                                return False
                                        return True
                                if placement == False:
                                        return True
                        else:
                                print("The column you've introduced is not on the board! Please, start again.")
                                return False
                else:
                        print("The row you've introduced is not on the board! Please, start again.")
                        return False

        def movePiece(self):
                while True:
                        decision = input("Do you want to make a move? [Y]/N: ")
                        decision = decision.capitalize()

                        if decision == "Y":
                                piece_row = int(input("Which row is the piece you want to move in?: (Please select a row from 0 to 7)\n"))
                                if self.validPlacement(piece_row, 0, False) == True:
                                        piece_column = int(input("Which column is the piece you want to move in?: (Please select a column from 0 to 7)\n"))
                                        if self.validPlacement(piece_row, piece_column, True) == True:
                                                piece = self.board[piece_row][piece_column]
                                                self.board[piece_row][piece_column] = " "
                                                final_row = int(input("Which row do you want to move your piece into?: (Please select a row from 0 to 7)\n"))
                                                if self.validPlacement(final_row, 0, False) == True:
                                                        final_column = int(input("Which column do you want to move your piece into?: (Please select a column from 0 to 7)\n"))
                                                        if self.validPlacement(final_row, final_column, False) == True:
                                                                self.board[final_row][final_column] = piece
                                                                self.saveBoard()
                                                                self.movement = self.movement + 1
                                                                self.printBoard(self.movement + 1)

                        if decision == "N":
                                if self.movement != 0:
                                        while True:
                                                question = input("Do you want to review any movements of the game? [Y]/N: ")
                                                question = question.capitalize()

                                                if self.movement > 1:
                                                        num_mov = "movements"
                                                else:
                                                        num_mov = "movement"

                                                if question == "Y":
                                                        review = int(input("Which movement do you want to review? (Please bear in mind that you've done " + str(self.movement) + " " + str(num_mov) + "): "))
                                                        if review in range(self.movement + 1):
                                                                self.printBoard(review + 1)
                                                        else:
                                                                print("There isn't a movement like that! Please check that you haven't introduced a number higher than " + str(self.movement) + ".")
                                                if question == "N":
                                                        print("Thank you for playing chess! See you later!")
                                                        break
                                        break
                                else:
                                        print("Thank you for playing chess! See you later!")
                                        break

file_name = input("What name do you want to give to your chess game?: ")
chess_game = Chess(file_name)
chess_game.printBoard(1)
chess_game.movePiece()
