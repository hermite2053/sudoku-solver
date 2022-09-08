def subgrid_cells(grid_r, grid_c):
    '''
    return the list of cells belong to specified block.
    '''
    cells = []
    for r in range(3):
        for c in range(3):
            cells.append([3 * grid_r + r, 3 * grid_c + c])
    return cells


def row_cells(r):
    '''
    return the list of cells belong to specified row.
    '''
    cells = []
    for c in range(9):
        cells.append([r, c])
    return cells


def column_cells(c):
    '''
    return the list of cells belong to specified column.
    '''
    cells = []
    for r in range(9):
        cells.append([r, c])
    return cells


def same_row_cells(row, column):
    target_cells = []
    for i in range(9):
        if i is not column:
            target_cells.append([row, i])
    return target_cells


def same_column_cells(row, column):
    target_cells = []
    for i in range(9):
        if i is not row:
            target_cells.append([i, column])
    return target_cells


def exclusive_cells(row, column):
    target_cells = []
    r = int(row // 3 * 3)
    c = int(column // 3 * 3)
    for i in range(r, r+3):
        for j in range(c, c+3):
            if i is not row and j is not column:
                target_cells.append([i, j])
    target_cells = target_cells + same_row_cells(row, column)
    target_cells = target_cells + same_column_cells(row, column)
    return target_cells


def delete_candidate_number(cand_grid, target_cell_list, number):
    for i, j in target_cell_list:
        if number in cand_grid[i][j]:
            cand_grid[i][j].remove(number)


def identify_cell_number(cand_grid, target_cell, number):
    if len(cand_grid[target_cell[0]][target_cell[1]]) > 1:
        cand_grid[target_cell[0]][target_cell[1]] = []
        cand_grid[target_cell[0]][target_cell[1]].append(number)
