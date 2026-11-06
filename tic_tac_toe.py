import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def get_empty_boxes():
    empty_boxes = []
    for i in range(9):
        if board[i] == " ":
            empty_boxes.append(i)
    return empty_boxes

def computer_move(mark):
    empty_boxes = get_empty_boxes()
    choice = random.choice(empty_boxes)
    board[choice] = mark
    print("Computer put " + mark + " in box " + str(choice + 1))

def player_move(mark):
    while True:
        number = int(input("Choose a box (1-9): "))
        box = number - 1
        if board[box] == " ":
            board[box] = mark
            break
        else:
            print("That box is already taken. ")

winning_lines = [
    [0, 1, 2], [3, 4, 5],[6, 7, 8], [0, 3, 6], [1, 4, 7],  [2, 5, 8],  [0, 4, 8],  [2, 4, 6],  
]

def check_winner(mark):
    for line in winning_lines:
        a = line[0]
        b = line[1]
        c = line[2]
        if board[a] == mark and board[b] == mark and board[c] == mark:
            return True
    return False

player = "X"
computer = "O"

print_board()

while True:
    player_move(player)
    print_board()
    if check_winner(player):
        print("You win!")
        break
    if len(get_empty_boxes()) == 0:
        print("It's a draw!")
        break

    computer_move(computer)
    print_board()
    if check_winner(computer):
        print("Computer wins!")
        break
    if len(get_empty_boxes()) == 0:
        print("It's a draw!")
        break
