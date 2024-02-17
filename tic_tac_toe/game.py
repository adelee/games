def draw_board(board):
    print(
        f"  {board[1]} | {board[2]} | {board[3]}\n",
        f"-----------\n",
        f" {board[4]} | {board[5]} | {board[6]}\n",
        f"-----------\n",
        f" {board[7]} | {board[8]} | {board[9]}\n"
    )


def check_win(board):
    if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]):
        return True
    elif (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[3] == board[6] == board[9]):
        return True
    elif (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7]):
        return True


def check_draw(board):
    for i in board.values():
        if i not in ["X", "O"]:
            return False
    return True
