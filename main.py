import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("  A B C D E F G")
    for i, row in enumerate(board):
        print(f"{i + 1} " + " ".join(row))
