board = [['  ' for i in range(8)] for i in range(8)]

f = open("board.txt", "w")
f.write(print(board[0]),
        print(board[1]),
        print(board[2]),
        print(board[3]),
        print(board[4]),
        print(board[5]),
        print(board[6]),
        print(board[7]),
        )
f.close

f = open("board.txt", "r")
print(f.read())
