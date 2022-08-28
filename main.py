from operator import xor

sudoku_table_example = [
		[1, 2, 3, 4, 5, 6, 7, 8, 9],
		[4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 0, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [9, 1, 2, 3, 4, 5, 6, 7, 8]]

def print_sudoku_table(sudoku_table):
    for row_idx, row in enumerate(sudoku_table):
        for idx, elm in enumerate(row):
            if xor(0 <= idx <= 2 or 6 <= idx <= 8, 3 <= row_idx <= 5):
                print(f'\x1b[7m{elm}\x1b[0m', end='')
            else:
                print(f'{elm}', end='')
        print()

        
def block_list_linear(sudoku_table, row, column):
    block_list = []
    r = int(row // 3 * 3)
    c = int(column // 3 * 3)
    for i in range(r, r+3):
        for j in range(c, c+3):
            block_list.append(sudoku_table[i][j])
    return block_list


def candidates_list(sudoku_table, row, column):
    cand_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in sudoku_table[row]:
        if i == 0:
            continue
        else:
            try:
                cand_list.remove(i)
            except:
                continue
    for i in range(9):
        if i == 0:
            continue
        else:
            try:
                cand_list.remove(sudoku_table[i][column])
            except:
                continue
    for i in block_list_linear(sudoku_table, row, column):
        if i == 0:
            continue
        else:
            try:
                cand_list.remove(i)
            except:
                continue
    
    return cand_list


def is_solved(sudoku_table):
    for i in range(9):
        for j in range(9):
            if len(candidates_list(sudoku_table, i, j)) > 0:
                return False
    return True


print('problem:')
print_sudoku_table(sudoku_table_example)
while not is_solved(sudoku_table_example):
    for i in range(9):
        for j in range(9):
            if len(candidates_list(sudoku_table_example, i, j)) == 1:
                sudoku_table_example[i][j] = \
                    candidates_list(sudoku_table_example, i, j)[0]

print('Answer:')
print_sudoku_table(sudoku_table_example)
