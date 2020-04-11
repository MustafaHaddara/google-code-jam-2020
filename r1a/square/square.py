def get_interest_level(grid):
    interest = interest_level_round(grid)
    
    while remove_dead_dancers(grid):
        interest += interest_level_round(grid)
        grid = suppress_empties(grid)

    return interest

def suppress_empties(grid):
    # cols
    cols_to_kill = find_cols_to_kill(grid)

    # rows
    if len(cols_to_kill) == 0:
        newgrid = None
    else:
        newgrid = []

    for y,row in enumerate(grid):
        if row_is_empty(row):
            if newgrid is None:
                newgrid = grid[y-1:]
        else:
            if newgrid is not None:
                newgrid.append(suppress(row, cols_to_kill))
    
    if newgrid is None:
        return grid
    return newgrid

def suppress(row, cols_to_kill):
    if len(cols_to_kill) == 0:
        return row
    newrow = []
    for y,item in enumerate(row):
        if y in cols_to_kill:
            continue
        newrow.append(item)
    return newrow

def find_cols_to_kill(grid):
    cols = set()
    for x in range(len(grid[0])):
        if col_is_empty(grid, x):
            cols.add(x)
    return cols

def col_is_empty(grid, x):
    y = 0
    while y < len(grid):
        if grid[y][x] != 0:
            return False
        y += 1
    return True

def row_is_empty(row):
    for e in row:
        if e != 0:
            return False
    return True


def remove_dead_dancers(grid):
    to_kill = []
    for y,row in enumerate(grid):
        for x,skill in enumerate(row):
            if skill == 0:
                continue
            s = find_compass_neighbors_skill(x,y,grid)
            # print(x,y, skill, s)
            if skill < s:
                # print('dead!')
                # oh no i'm out
                to_kill.append([x,y])
    

    for dead in to_kill:
        x,y = dead
        grid[y][x] = 0

    # print(grid)

    return len(to_kill) != 0

def find_compass_neighbors_skill(x,y,grid):
    skills = []
    # up
    dy = y-1
    while dy >= 0:
        if grid[dy][x] != 0:
            skills.append(grid[dy][x])
            break
        dy -= 1

    # down
    dy = y+1
    while dy < len(grid):
        if grid[dy][x] != 0:
            skills.append(grid[dy][x])
            break
        dy += 1
    
    # right
    dx = x+1
    while dx < len(grid[0]):
        if grid[y][dx] != 0:
            skills.append(grid[y][dx])
            break
        dx += 1
    
    # left
    dx = x-1
    while dx >= 0:
        if grid[y][dx] != 0:
            skills.append(grid[y][dx])
            break
        dx -= 1

    # print(x,y, skills)

    if len(skills) == 0:
        return 0
    return sum(skills) / len(skills)

def interest_level_round(grid):
    return sum(sum(row) for row in grid)


def build_initial_grid():
    rows,cols = [int(i) for i in input().split()]
    grid = []
    for i in range(rows):
        grid.append( [int(i) for i in input().split()] )
    return grid

if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        grid = build_initial_grid()
        level = get_interest_level(grid)
        print("Case #{}: {}".format(i+1, level))
