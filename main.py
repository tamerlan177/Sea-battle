import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    print("  A B C D E F G")
    for i, row in enumerate(board):
        print(f"{i + 1} " + " ".join(row))

def is_valid_position(board, row, col, length, orientation):
    for i in range(length):
        r = row + (i if orientation == "V" else 0)
        c = col + (i if orientation == "H" else 0)
        if r < 0 or r >= 7 or c < 0 or c >= 7 or board[r][c] != ".":
            return False

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 7 and 0 <= nc < 7 and board[nr][nc] != ".":
                    return False
    return True

# Placing ships
def place_ship(board, length):
    while True:
        row = random.randint(0, 6)
        col = random.randint(0, 6)
        orientation = random.choice(["H", "V"])
        if is_valid_position(board, row, col, length, orientation):
            for i in range(length):
                r = row + (i if orientation == "V" else 0)
                c = col + (i if orientation == "H" else 0)
                board[r][c] = str(length)
            break

# Setting up the board
def setup_board():
    board = [["." for _ in range(7)] for _ in range(7)]
    place_ship(board, 3)  
    place_ship(board, 2) 
    place_ship(board, 2)  
    for _ in range(4):    
        place_ship(board, 1)
    return board

# Shooting
def shoot(board, display, row, col):
    if board[row][col] != ".":
        hit_ship = board[row][col]
        board[row][col] = "."
        display[row][col] = "X"
        if all(board[r][c] != hit_ship for r in range(7) for c in range(7)):
            for r in range(7):
                for c in range(7):
                    if display[r][c] == "X" and board[r][c] == ".":
                        display[r][c] = "S"
            return "sunk"
        return "hit"
    else:
        display[row][col] = "O"
        return "miss"

# Main function
def play_game():
    clear_screen()
    name = input("Enter your name: ")
    scores = []

    while True:
        hidden_board = setup_board()
        display_board = [["." for _ in range(7)] for _ in range(7)]
        shots = 0
        ships_remaining = 9 

        while ships_remaining > 0:
            clear_screen()
            print_board(display_board)
            print(f"Shots fired: {shots}")

            move = input("Enter your shot (e.g., B5): ").upper()
            if len(move) < 2 or move[0] not in "ABCDEFG" or not move[1:].isdigit():
                print("Invalid input! Please enter a valid position like B5.")
                continue

            col = "ABCDEFG".index(move[0])
            row = int(move[1:]) - 1

            if row < 0 or row >= 7 or col < 0 or col >= 7:
                print("Out of bounds! Try again.")
                continue

            if display_board[row][col] != ".":
                print("You already shot there! Try again.")
                continue

            shots += 1
            result = shoot(hidden_board, display_board, row, col)
            if result == "hit":
                print("You hit a ship!")
            elif result == "sunk":
                print("You sunk a ship!")
                ships_remaining -= 1
            else:
                print("Miss!")

        clear_screen()
        print(f"Congratulations, {name}! You won in {shots} shots.")
        scores.append((name, shots))
        scores.sort(key=lambda x: x[1])

        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            break

    clear_screen()
    print("Final Leaderboard:")
    for rank, (player, score) in enumerate(scores, 1):
        print(f"{rank}. {player} - {score} shots")
    print("Thanks for playing!")

play_game()

