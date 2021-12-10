class ChessBoard():
        board = []

        def __init__(self) -> None:
                self.board = [['  ' for i in range(8)] for i in range(8)]

                self.chessPieces()

                f = open("board.txt", "w", encoding="utf8")
                for i in range(8):
                        for j in range(8):
                                f.write(self.board[i][j])
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
                f = open("board.txt", "a", encoding="utf8")
                for i in range(8):
                        for j in range(8):
                                f.write(self.board[i][j])
                        f.write("\n")

                f.close

        def printBoard(self):
                f = open("board.txt", "r", encoding="utf8")
                for line in f:        
                        print(line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3] + "\t" + line[4] + "\t" + line[5] + "\t" + line[6] + "\t" + line[7])

chessBoard = ChessBoard()
chessBoard.printBoard()