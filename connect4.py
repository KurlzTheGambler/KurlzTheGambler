
def makeGrid(nRows ,nCols):
    board = []
    if nRows > 10:
        print('Rows and Columns should be 4 <= nRows <=10')
    elif nRows < 4:
        print('Rows and Columns should be 4 <= nRows <=10')
    elif nCols > 10:
        print('Rows and Columns should be 4 <= nColumns <=10')
    elif nCols < 4:
        print('Rows and Columns should be 4 nColumns <=10')
    else:
        for _ in range(nRows):
            board_row = []
            for _ in range(nCols):
                board_row.append('empty')
            board.append(board_row)

        return board

def play(grid , column , checker):
    for row in reversed(grid):
        if row[int(column)] == "empty":
            row[int(column)] = checker
            return True
    return False

def win(grid , column):
    row = len(grid)
    tile = 'red'
    tile2 = 'black'
    # check for horizontal win
    for y in range(len(grid[column])):
        for x in range(row - 3):
            if grid[x][y] == tile and grid[x+1][y] == tile and grid[x+2][y] == tile and grid[x+3][y] == tile:
                return tile
            elif grid[x][y] == tile2 and grid[x+1][y] == tile2 and grid[x+2][y] == tile2 and grid[x+3][y] == tile2:
                return tile2

    # check for vertical win
    for x in range(row):
        for y in range(len(grid[column]) - 3):
            if grid[x][y] == tile and grid[x][y+1] == tile and grid[x][y+2] == tile and grid[x][y+3] == tile:
                return tile
            elif grid[x][y] == tile2 and grid[x][y+1] == tile2 and grid[x][y+2] == tile2 and grid[x][y+3] == tile2:
                return tile2

    # check for diagonal win
    for x in range(row - 3):
        for y in range(3, len(grid[column])):
            if grid[x][y] == tile and grid[x+1][y-1] == tile and grid[x+2][y-2] == tile and grid[x+3][y-3] == tile:
                return tile
            elif grid[x][y] == tile2 and grid[x+1][y-1] == tile2 and grid[x+2][y-2] == tile2 and grid[x+3][y-3] == tile2:
                return tile2
    for x in range(row - 3):
        for y in range(len(grid[column]) - 3):
            if grid[x][y] == tile and grid[x+1][y+1] == tile and grid[x+2][y+2] == tile and grid[x+3][y+3] == tile:
                return tile
            elif grid[x][y] == tile2 and grid[x+1][y+1] == tile2 and grid[x+2][y+2] == tile2 and grid[x+3][y+3] == tile2:
                return tile2

    return 'empty'





def toString(grid):
    game =''
    for i in range(len(grid)):
        game = game +"|"
        for j in range(len(grid)):
            if grid[i][j] =='red':
                game = game + 'X'
            elif grid[i][j] == 'black':
                game = game + 'O'
            else:
               game = game + ' '
        game = game + "|"+str(i) + '\n'
    game += '+'
    for i in range(len(grid)):
        game += '-'
    game += '+'
    game += '\n'
    game += ' '
    for i in range(len(grid)):
        game = '\n'+ game + str(i)

    return game

