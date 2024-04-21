'''Minesweeper program

The minesweeper function takes in a grid of # and -, where each hash
represents a mine and each dash represents a mine-free spot. It returns
a grid where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e., horizontally, vertically,
and diagonally

It is important that the grid must be 3x3 or greater
'''

my_grid = [ ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"] ]

# First row
def grid_first_row(value, index_value, index_row, grid, new_grid):
    '''
    Specific to values that are at the top left and right of a grid.
    Checks how many mines are adjacent to a mine free spot and appends
    this value to its specific row (list) within the new grid and
    returns the new grid
    '''

    count = 0  # Store total number of mines around a mine-free spot
    # Flags are to check if an 'if condition' has already been met
    w_or_e_flag = 0  # West or East flag
    s_flag = 0
    se_or_sw_flag = 0  # South East or South West flag

    # Store position of adjacent values
    s_position = grid[index_row+1][index_value]  # South

    # First value in grid
    if (index_row == 0) and (index_value == 0):
        w_or_e_position = grid[index_row][index_value + 1]  # East
        # South East
        se_or_sw_position = grid[index_row+1][index_value+1]

    # Last value in grid
    elif (index_row == 0 and (index_value == len(grid[index_row]) - 1)):
        w_or_e_position = grid[index_row][index_value-1]  # West
        # South West
        se_or_sw_position = grid[index_row+1][index_value-1]

    # Range number must match number of positions above
    for _ in range(3):
        if (value != w_or_e_position) and (w_or_e_flag == 0):
            count+=1
            w_or_e_flag = 1
        elif (value != s_position) and (s_flag == 0):
            count+=1
            s_flag = 1
        elif (value != se_or_sw_position) and (se_or_sw_flag == 0):
            count+=1
            se_or_sw_flag = 1

    new_grid[index_row].append(count)
    return new_grid

# Last row
def grid_last_row(value, index_value, index_row, grid, new_grid):
    '''
    Specific to values that are at the bottom left and right of a
    grid. Checks how many mines are adjacent to a mine free spot and
    appends this value to its specific row (list) within the new grid
    and returns the new grid
    '''

    count = 0  # Store total number of mines around a mine-free spot
    # Flags are to check if an 'if condition' has already been met
    w_or_e_flag = 0  # West or East flag
    n_flag = 0
    ne_or_nw_flag = 0  # North East or North West flag

    # Store position of adjacent values
    n_position = grid[index_row-1][index_value]  # North

    if index_value == 0:  # Bottom left values in grid
        w_or_e_position = grid[index_row][index_value+1]  # East
        # North East
        ne_or_nw_position = grid[index_row-1][index_value+1]

    else:  # Bottom right values in grid
        w_or_e_position = grid[index_row][index_value-1]  # West
        # North West
        ne_or_nw_position = grid[index_row-1][index_value-1]

    # Range number must match number of positions above
    for _ in range(3):
        if (value != w_or_e_position) and (w_or_e_flag == 0):
            count+=1
            w_or_e_flag = 1
        elif (value != n_position) and (n_flag == 0):
            count+=1
            n_flag = 1
        elif (value != ne_or_nw_position) and (ne_or_nw_flag == 0):
            count+=1
            ne_or_nw_flag = 1

    new_grid[index_row].append(count)
    return new_grid

# Grid Sides
def grid_side_values(value, index_value, index_row, grid, new_grid):
    '''
    Specific to values that are at the side of a grid. Checks how
    many mines are adjacent to a mine free spot and appends this value
    to its specific row (list) within the new grid and returns the
    new grid
    '''

    count = 0  # Store total number of mines around a mine-free spot
    # Flags are to check if an 'if condition' has already been met
    n_flag = 0
    ne_or_nw_flag = 0  # North East or North West flag
    w_or_e_flag = 0  # West or East Flag
    se_or_sw_flag = 0  # South East or South West flag
    s_flag = 0

    # Store position of adjacent values
    n_position = grid[index_row-1][index_value]  # North
    s_position = grid[index_row+1][index_value]  # South

    if index_value == 0:  # Left side values in grid
        w_or_e_position = grid[index_row][index_value+1]  # East
        # North East
        ne_or_nw_position = grid[index_row-1][index_value+1]
        # South East
        se_or_sw_position = grid[index_row+1][index_value+1]

    else:  # Right side values in grid
        w_or_e_position = grid[index_row][index_value-1]  # West
        # North West
        ne_or_nw_position = grid[index_row-1][index_value-1]
        # South West
        se_or_sw_position = grid[index_row+1][index_value-1]

    # Range number must match number of positions above
    for _ in range(5):
        if (value != w_or_e_position) and (w_or_e_flag == 0):
            count+=1
            w_or_e_flag = 1
        elif (value != n_position) and (n_flag == 0):
            count+=1
            n_flag = 1
        elif (value != ne_or_nw_position) and (ne_or_nw_flag == 0):
            count+=1
            ne_or_nw_flag = 1
        elif (value != s_position) and (s_flag == 0):
            count+=1
            s_flag = 1
        elif (value != se_or_sw_position) and (se_or_sw_flag == 0):
            count+=1
            se_or_sw_flag = 1

    new_grid[index_row].append(count)
    return new_grid

# Top and bottom
def grid_top_and_bottom_values(value, index_value, index_row, grid, new_grid):
    '''
    Specific to values that are at the top and bottom of a grid.
    Checks how many mines are adjacent to a mine free spot and appends
    this value to its specific row (list) within the new grid and
    returns the new grid
    '''

    count = 0  # Store total number of mines around a mine-free spot
    # Flags are to check if an 'if condition' has already been met
    e_flag = 0
    w_flag = 0
    n_or_s_flag = 0  # North or South flag
    se_or_ne_flag = 0  # South East or South West flag
    nw_or_sw_flag = 0  # North West or South West flag

    # Store position of adjacent values
    e_position = grid[index_row][index_value+1]  # East
    w_position = grid[index_row][index_value-1]  # West

    if index_row == 0:  # Top grid values
        n_or_s_position = grid[index_row+1][index_value]  # South
        # South East
        se_or_ne_position = grid[index_row+1][index_value+1]
        # South West
        nw_or_sw_position = grid[index_row+1][index_value-1]

    else:  # Bottom grid values
        n_or_s_position = grid[index_row-1][index_value]  # North
        # North East
        se_or_ne_position = grid[index_row-1][index_value+1]
        # North West
        nw_or_sw_position = grid[index_row-1][index_value-1]

    # Range number must match number of positions above
    for _ in range(5):
        if (value != e_position) and (e_flag == 0):
            count+=1
            e_flag = 1
        elif (value != w_position) and (w_flag == 0):
            count+=1
            w_flag = 1
        elif (value != n_or_s_position) and (n_or_s_flag == 0):
            count+=1
            n_or_s_flag = 1
        elif (value != se_or_ne_position) and (se_or_ne_flag == 0):
            count+=1
            se_or_ne_flag = 1
        elif (value != nw_or_sw_position) and (nw_or_sw_flag == 0):
            count+=1
            nw_or_sw_flag = 1

    new_grid[index_row].append(count)
    return new_grid

# Center values
def grid_center_values(value, index_value, index_row, grid, new_grid):
    '''
    Specific to values that are in the center of grid. It checks how
    many mines are adjacent to a mine free spot and appends this value
    to its specific row (list) within the new grid and returns
    the new grid
    '''

    count = 0  # Store total number of mines around a mine-free spot
    # Flags are to check if an 'if condition' has already been met
    e_flag = 0
    w_flag = 0
    n_flag = 0
    s_flag = 0
    s_e_flag = 0
    s_w_flag = 0
    n_e_flag = 0
    n_w_flag = 0

    # Store position of adjacent values
    e_position = grid[index_row][index_value+1]
    w_position = grid[index_row][index_value-1]
    n_position = grid[index_row-1][index_value]
    s_position = grid[index_row+1][index_value]
    s_e_position = grid[index_row+1][index_value+1]
    s_w_position = grid[index_row+1][index_value-1]
    n_e_position = grid[index_row-1][index_value+1]
    n_w_position = grid[index_row-1][index_value-1]

    # Range number must match number of positions above
    for _ in range(8):
        if (value != e_position) and (e_flag == 0):
            count+=1
            e_flag = 1
        elif (value != w_position) and (w_flag == 0):
            count+=1
            w_flag = 1
        elif (value != n_position) and (n_flag == 0):
            count+=1
            n_flag = 1
        elif (value != s_position) and (s_flag == 0):
            count+=1
            s_flag = 1
        elif (value != s_e_position) and (s_e_flag == 0):
            count+=1
            s_e_flag = 1
        elif (value != s_w_position) and (s_w_flag == 0):
            count+=1
            s_w_flag = 1
        elif (value != n_e_position) and (n_e_flag == 0):
            count+=1
            n_e_flag = 1
        elif (value != n_w_position) and (n_w_flag == 0):
            count+=1
            n_w_flag = 1

    new_grid[index_row].append(count)
    return new_grid

# Driver function
def mine_sweeper(grid):
    '''
    Takes in a grid and returns a new grid where each dash in the
    input grid is replaced by a digit, indicating the number of mines
    immediately adjacent to the spot
    '''

    new_grid = [[]]  # To store end result
    # Store total number of rows in grid
    grid_rows_total = len(grid) - 1

    # Create x amount of lists within new grid to store values
    for _ in range(grid_rows_total):
        new_grid.append([])

    for index_row, row in enumerate(grid):  # Loop over each row in grid
        # Store grid row length (how many values in a row)
        grid_row_length = len(grid[index_row])-1

        # Loop over each value in each row
        for index_value, value in enumerate(row):
            if value == "#":
                # Append value to its relevant row
                new_grid[index_row].append(value)

        # First or last value in the first row
            elif ((index_row == 0 and index_value == 0)
                or (index_row == 0) and index_value == grid_row_length):
                grid_first_row(value, index_value, index_row, grid, new_grid)

        # First or last value in the last row
            elif ((index_row == grid_rows_total and index_value == 0)
                or (index_row == grid_rows_total
                    and index_value == grid_row_length)):
                grid_last_row(value, index_value, index_row, grid, new_grid)

        # Furthest left or right hand side of the grid
            elif index_value in {0, grid_row_length}:
                grid_side_values(value,
                                 index_value,
                                 index_row,
                                 grid,
                                 new_grid)

        # Top or bottom of the grid
            elif (index_value in range(1, grid_row_length)
            and index_row in {0, grid_rows_total}):
                grid_top_and_bottom_values(value,
                                           index_value,
                                           index_row,
                                           grid,
                                           new_grid)

        # Center of the grid
            else:
                grid_center_values(value,
                                   index_value,
                                   index_row,
                                   grid,
                                   new_grid)

    return new_grid

result = mine_sweeper(my_grid)

for grid_row in result:
    print(grid_row)

# IGNORE: NOTES

# W position - current_row / current_col - 1
# E position - current_row / current_col + 1
# S position - current_row + 1 / current_col
# N position - current_row - 1 / current_col
# NE position - current_row - 1 / current_col + 1
# SE position - current_row + 1 / current_col + 1
# SW position - current_row + 1 / current_col - 1
# NW position - current_row - 1 / current_col - 1
# Current position - current_row / current_col
