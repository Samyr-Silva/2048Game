import random

def comecar_jogo():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        x, y = random.choice(empty_cells)
        board[x][y] = 2 if random.random() < 0.9 else 4

def compress(board):
    new_board = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][pos] = board[i][j]
                pos += 1
    return new_board

def merge(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def move_left(board):
    compressed_board = compress(board)
    merged_board = merge(compressed_board)
    final_board = compress(merged_board)
    return final_board

def move_right(board):
    reversed_board = [row[::-1] for row in board]
    moved_board = move_left(reversed_board)
    return [row[::-1] for row in moved_board]

def move_up(board):
    transposed_board = [[board[j][i] for j in range(4)] for i in range(4)]
    moved_board = move_left(transposed_board)
    return [[moved_board[j][i] for j in range(4)] for i in range(4)]

def move_down(board):
    transposed_board = [[board[j][i] for j in range(4)] for i in range(4)]
    moved_board = move_right(transposed_board)
    return [[moved_board[j][i] for j in range(4)] for i in range(4)]

def check_game_status(board):
    if any(2048 in row for row in board):
        return 'WON'
    if any(0 in row for row in board):
        return 'CONTINUE'
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return 'CONTINUE'
    return 'LOST'

def print_board(board):
    for row in board:
        print('\t'.join(map(str, row)))
    print()

def main():
    board = comecar_jogo()
    print_board(board)
    while True:
        move = input("Enter move (WASD): ").upper()
        if move in ['W', 'A', 'S', 'D']:
            if move == 'W':
                board = move_up(board)
            elif move == 'A':
                board = move_left(board)
            elif move == 'S':
                board = move_down(board)
            elif move == 'D':
                board = move_right(board)

            add_new_tile(board)
            print_board(board)

            status = check_game_status(board)
            if status == 'WON':
                print("Congratulations! You've won!")
                break
            elif status == 'LOST':
                print("Game Over! You've lost!")
                break
        else:
            print("Invalid move! Please enter W, A, S, or D.")

if __name__ == "__main__":
    main()

