import random

# Initialize the board as a list of 9 empty strings
board = [" "] * 9

# Check if a player has won
def win(n):
    condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for i in condition:
        if board[i[0]] == board[i[1]] == board[i[2]] == n:
            return True
    return False

# Check if the board is full and it's a draw
def draw():
    return " " not in board

# Simulate computer move
def computer():
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)  # Randomly choose an empty spot
    board[move] = '0'
    printBoard()
    if win('0'):
        print("Computer is the winner!")
        return True
    return False

# Human input for making a move
def humaninput(ipt, index):
    if board[index] == " ":
        board[index] = ipt
    else:
        print(f"Index {index} is already occupied. Choose another index.")

# Print the game board
def printBoard():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

# Main gameplay loop
def play():
    print("Choose the game mode:\nVs Computer - 1\nVs Human - 2")
    t = int(input("Enter the player: "))
    printBoard()

    if t == 1:
        while not draw():
            a = input("Enter your choice ('X' or 'O'): ")
            ind = int(input("Enter index (0-8): "))
            if 0 <= ind <= 8 and board[ind] == " ":
                humaninput(a, ind)
            else:
                print("Invalid input. Please choose an empty index between 0 and 8.")
                continue
            
            if win(a):
                printBoard()
                print(f"User {a} is the winner!")
                break

            if draw():
                printBoard()
                print("Game over! It's a draw.")
                break

            if computer():
                break

    elif t == 2:
        while not draw():
            a = input("Enter your choice ('X' or 'O'): ")
            ind = int(input("Enter index (0-8): "))
            if 0 <= ind <= 8 and board[ind] == " ":
                humaninput(a, ind)
            else:
                print("Invalid input. Please choose an empty index between 0 and 8.")
                continue

            if win(a):
                printBoard()
                print(f"User {a} is the winner!")
                break

            if draw():
                printBoard()
                print("Game over! It's a draw.")
                break

            printBoard()

# Start the game
play()

