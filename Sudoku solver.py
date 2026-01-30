def print_grid(grid):
    print("\n" + "=" * 37)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 37)
        
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += " | "
            row += str(grid[i][j]) + " "
        print(row)
    print("=" * 37 + "\n")


def is_valid_grid(grid):
    if len(grid) != 9:
        print("Error: Grid must have exactly 9 rows")
        return False
    
    for row in grid:
        if len(row) != 9:
            print("Error: Each row must have exactly 9 columns")
            return False
    
    for i in range(9):
        for j in range(9):
            if not isinstance(grid[i][j], int) or grid[i][j] < 0 or grid[i][j] > 9:
                print(f"Error: Invalid value at position ({i}, {j}). Must be integer 0-9")
                return False
    
    for i in range(9):
        row_values = [grid[i][j] for j in range(9) if grid[i][j] != 0]
        if len(row_values) != len(set(row_values)):
            print(f"Error: Duplicate values found in row {i + 1}")
            return False
    
    for j in range(9):
        col_values = [grid[i][j] for i in range(9) if grid[i][j] != 0]
        if len(col_values) != len(set(col_values)):
            print(f"Error: Duplicate values found in column {j + 1}")
            return False
    
    # Check for duplicates in 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            box_values = []
            for i in range(box_row * 3, box_row * 3 + 3):
                for j in range(box_col * 3, box_col * 3 + 3):
                    if grid[i][j] != 0:
                        box_values.append(grid[i][j])
            if len(box_values) != len(set(box_values)):
                print(f"Error: Duplicate values found in 3x3 box at position ({box_row}, {box_col})")
                return False
    
    return True


def is_safe(grid, row, col, num):
    for j in range(9):
        if grid[row][j] == num:
            return False
    
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True


def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def solve_sudoku(grid):
    empty = find_empty_cell(grid)
    
    if empty is None:
        return True
    
    row, col = empty
    
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0
    
    return False


def main():
    print("=" * 50)
    print("SUDOKU SOLVER - BACKTRACKING ALGORITHM")
    print("=" * 50)
    
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("\nORIGINAL SUDOKU PUZZLE:")
    print_grid(sudoku_grid)
    
    if not is_valid_grid(sudoku_grid):
        print("Invalid Sudoku grid! Please check the input.")
        return
    
    print("Solving the puzzle using backtracking algorithm...")
    print("Please wait...\n")
    
    if solve_sudoku(sudoku_grid):
        print("SUCCESS! Sudoku puzzle solved!")
        print("\nSOLVED SUDOKU GRID:")
        print_grid(sudoku_grid)
    else:
        print("NO SOLUTION EXISTS for this Sudoku puzzle!")
        print("The puzzle may be invalid or unsolvable.")
    
    print("\n" + "=" * 50)
    print("TESTING WITH AN UNSOLVABLE PUZZLE:")
    print("=" * 50)
    
    unsolvable_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 5]  
    ]
    
    print("\nUNSOLVABLE PUZZLE:")
    print_grid(unsolvable_grid)
    
    if not is_valid_grid(unsolvable_grid):
        print("Grid validation failed - contains conflicts!")
    elif solve_sudoku(unsolvable_grid):
        print("Puzzle solved!")
        print_grid(unsolvable_grid)
    else:
        print("NO SOLUTION EXISTS for this puzzle!")


if __name__ == "__main__":
    main()
