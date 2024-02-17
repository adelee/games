import art
from game import draw_board, check_win, check_draw
import os

board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

players = ["X", "O"]
player = 0
play = True

while play:
    print(art.logo)
    draw_board(board)
    player = player % 2 + 1

    choice = input(f"Player {player} - Choose a position or type 'q' to quit: ")
    if choice == "q":
        play = False
    elif choice not in board.values():
        print("Invalid entry")
        play = False
    else:
        board[int(choice)] = players[player-1]
        # os.system("cls" if os.name == "nt" else "clear")
        draw_board(board)

    if check_win(board):
        print(f"Player {player} won!")
        play = False
    elif check_draw(board):
        print("It's a draw!")
        play = False
