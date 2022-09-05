from operator import xor

def input_sudoku_table():
    input_sudoku_table = []
    for i in range(9):
        input_sudoku_table.append(list(map(int, input().split())))
    return input_sudoku_table


def print_sudoku_table(sudoku_table):
    for row_idx, row in enumerate(sudoku_table):
        for idx, elm in enumerate(row):
            if xor(0 <= idx <= 2 or 6 <= idx <= 8, 3 <= row_idx <= 5):
                print(f'\x1b[7m{elm}\x1b[0m', end='')
            else:
                print(f'{elm}', end='')
        print()

sudoku_table_example = [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 0, 6, 7, 8, 0, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 0, 5, 6, 7, 0, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [9, 1, 2, 3, 4, 5, 6, 7, 8]]
