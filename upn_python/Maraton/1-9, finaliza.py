import random

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[0][0], board[0][1], board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1][0], board[1][1], board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[2][0], board[2][1], board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    move = 0
    while move not in free_fields:
        move = int(input("Ingresa tu movimiento (1-9): "))
    board[(move-1)//3][(move-1)%3] = 'O'
    
def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_fields.append((i,j))
    return free_fields

def victory_for(board, sign):
    if (board[0][0] == board[0][1] == board[0][2] == sign or
        board[1][0] == board[1][1] == board[1][2] == sign or
        board[2][0] == board[2][1] == board[2][2] == sign or
        board[0][0] == board[1][0] == board[2][0] == sign or
        board[0][1] == board[1][1] == board[2][1] == sign or
        board[0][2] == board[1][2] == board[2][2] == sign or
        board[0][0] == board[1][1] == board[2][2] == sign or
        board[0][2] == board[1][1] == board[2][0] == sign):
        return True
    else:
        return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = random.choice(free_fields)
    board[move[0]][move[1]] = 'X'

board = [['1','2','3'],['4','X','6'],['7','8','9']]
display_board(board)
while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("¡Felicidades! ¡Ganaste!")
        break
    if make_list_of_free_fields(board) == []:
        print("¡Empate!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("¡Lo siento! ¡Perdiste!")
        break
