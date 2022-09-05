from user_io import *
import copy

def initial_candidate_sudoku_table():
    cell_cand = []
    row = []
    table = []
    for i in range(1, 10):
        cell_cand.append(i)
    for i in range(9):
        row.append(copy.deepcopy(cell_cand))
    for i in range(9):
        table.append(copy.deepcopy(row))
    return table


def target_cells_belonging_row(row, column):
    target_cells = []
    for i in range(9):
        if i is not column:
            target_cells.append([row, i])
    return target_cells


def target_cells_belonging_column(row, column):
    target_cells = []
    for i in range(9):
        if i is not row:
            target_cells.append([i, column])
    return target_cells


def target_cells(row, column):
    target_cells = []
    r = int(row // 3 * 3)
    c = int(column // 3 * 3)
    for i in range(r, r+3):
        for j in range(c, c+3):
            if i is not row and j is not column:
                target_cells.append([i, j])
    target_cells = target_cells + target_cells_belonging_column(row, column)
    target_cells = target_cells + target_cells_belonging_row(row, column)
    return target_cells


def main():
    cand_sudoku_table = initial_candidate_sudoku_table()
    prob_sudoku_table = []

    # prob_sudoku_table = input_sudoku_table()
    prob_sudoku_table = sudoku_table_example

    for i in range(9):
        for j in range(9):
            if prob_sudoku_table[i][j] != 0:
                cand_sudoku_table[i][j] = []
                cand_sudoku_table[i][j].append(prob_sudoku_table[i][j])

    for z in range(100):  # cycle limit
        for i in range(9):
            for j in range(9):
                c = list(cand_sudoku_table[i][j])
                if len(c) == 1:
                    remove_target = target_cells(i, j)
                    for x, y in remove_target:
                        if c[0] in cand_sudoku_table[x][y]:
                            cand_sudoku_table[x][y].remove(c[0])

    print_sudoku_table(cand_sudoku_table)


if __name__ == '__main__':
    main()
