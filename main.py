from logic import *
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


def find_cell(sudoku_table, search_list, num):
    found_list = []
    for i, j in search_list:
        if num in sudoku_table[i][j]:
            found_list.append([i, j])
    return found_list


def chk(sudoku_table):
    for i in range(9):
        for j in range(9):
            if len(sudoku_table[i][j]) > 1:
                return False
    return True

def main():
    cand_sudoku_table = initial_candidate_sudoku_table()
    prob_sudoku_table = []

    prob_sudoku_table = input_sudoku_table()

    for i in range(9):
        for j in range(9):
            if prob_sudoku_table[i][j] != 0:
                cand_sudoku_table[i][j] = []
                cand_sudoku_table[i][j].append(prob_sudoku_table[i][j])

    for loop in range(50):  # cycle limit
        # delete candidates by using confirmed cell 9x9
        for i in range(9):
            for j in range(9):
                c = list(cand_sudoku_table[i][j])
                if len(c) == 1:
                    delete_candidate_number(cand_sudoku_table, exclusive_cells(i, j), c[0])
        for n in range(1, 10):
            for i in range(3):
                for j in range(3):
                    cell = find_cell(cand_sudoku_table, subgrid_cells(i, j), n)
                    if len(cell) == 1:
                        # search a cell that can contain the number in subgrid
                        # and then set the number.
                        identify_cell_number(cand_sudoku_table, cell[0], n)
                    elif len(cell) == 2:
                        if cell[0][0] == cell[1][0]:
                            # same row
                            tg = row_cells(cell[0][0])
                            tg.remove(cell[0])
                            tg.remove(cell[1])
                            delete_candidate_number(cand_sudoku_table, tg, n)
                        elif cell[0][1] == cell[1][1]:
                            # same column
                            tg = column_cells(cell[0][1])
                            tg.remove(cell[0])
                            tg.remove(cell[1])
                            delete_candidate_number(cand_sudoku_table, tg, n)
                    elif len(cell) == 3:
                        if cell[0][0] == cell[1][0] == cell[2][0]:
                            # same row
                            tg = row_cells(cell[0][0])
                            tg.remove(cell[0])
                            tg.remove(cell[1])
                            tg.remove(cell[2])
                            delete_candidate_number(cand_sudoku_table, tg, n)
                        elif cell[0][1] == cell[1][1] == cell[2][1]:
                            # same column
                            tg = column_cells(cell[0][1])
                            tg.remove(cell[0])
                            tg.remove(cell[1])
                            tg.remove(cell[2])
                            delete_candidate_number(cand_sudoku_table, tg, n)
            # search a cell that can contain the number in row
            # and then set the number.
            for i in range(9):
                cell = find_cell(cand_sudoku_table, row_cells(i), n)
                if len(cell) == 1:
                    identify_cell_number(cand_sudoku_table, cell[0], n)
            # search a cell that can contain the number in column
            # and then set the number.
            for i in range(9):
                cell = find_cell(cand_sudoku_table, column_cells(i), n)
                if len(cell) == 1:
                    identify_cell_number(cand_sudoku_table, cell[0], n)

        if chk(cand_sudoku_table) == True:
            break

    print_sudoku_table(cand_sudoku_table)


if __name__ == '__main__':
    main()
