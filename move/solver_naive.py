import copy,os
from itertools import product
from PIL import Image

def getQueValue(pixel):
    #print pixel
    if pixel == (152, 152, 152, 255):
        return 'b'
    elif pixel == (0, 211, 237, 255):
        return '1'
    elif pixel == (255, 0, 71, 255):
        return '2'
    elif pixel == (85, 255, 146, 255):
        return '3'
    else:
        return '-'

def getAnsValue(pixel):
    #print pixel
    if pixel == (152, 152, 152, 255):
        return 'b'
    elif pixel == (8, 137, 154, 255) or pixel == (10, 119, 133,255):
        return '1'
    elif pixel == (138, 13, 50, 255) or pixel == (161, 10, 54, 255):
        return '2'
    elif pixel == (53, 141, 88, 255) or pixel == (59, 163, 99, 255):
        return '3'
    else:
        return '-'

def parseImage(name,size):
    im = Image.open(name)
    q = [[0 for x in range(size)] for x in range(size)]
    a = [[0 for x in range(size)] for x in range(size)]
    if size == 3:
        x = 0
        y = 240
        for i in range(3):
            x = 0
            for j in range(3):
                a[i][j] = getAnsValue(im.getpixel((x+50,y+50)))
                q[i][j] = getQueValue(im.getpixel((x+180,y+180)))
                x += 360
            y += 360       
    #print q, a
    return q, a

def moveLeft(temp_grid):
    grid_size = len(temp_grid)
    flag=False
    for i in range(3):
        for j in range(1,grid_size):
            if temp_grid[i][j-1] == '-' and temp_grid[i][j]!='-' and temp_grid[i][j]!='b':
                temp_grid[i][j-1] = temp_grid[i][j]
                temp_grid[i][j] = '-'
                flag=True
    return flag

def moveRight(temp_grid):
    grid_size = len(temp_grid)
    flag=False
    for i in range(3):
        for j in range(grid_size-2,-1,-1):
            if temp_grid[i][j+1] == '-' and temp_grid[i][j]!='-' and temp_grid[i][j]!='b':
                temp_grid[i][j+1] = temp_grid[i][j]
                temp_grid[i][j] = '-'
                flag=True
    return flag

def moveUp(temp_grid):
    grid_size = len(temp_grid)   
    flag=False
    for i in range(1,grid_size):
        for j in range(grid_size):
            if temp_grid[i-1][j] == '-' and temp_grid[i][j]!='-' and temp_grid[i][j]!='b':
                temp_grid[i-1][j] = temp_grid[i][j]
                temp_grid[i][j] = '-'
                flag=True
    return flag

def moveDown(temp_grid):
    grid_size = len(temp_grid)
    flag=False
    for i in range(grid_size-2,-1,-1):
        for j in range(grid_size):
            if temp_grid[i+1][j] == '-' and temp_grid[i][j]!='-' and temp_grid[i][j]!='b':
                temp_grid[i+1][j] = temp_grid[i][j]
                temp_grid[i][j] = '-'
                flag=True
    return flag

def solve(que_grid,ans_grid,no_of_moves = 3):
    for no_of_moves in range(3,15):
        for permutation in list(product(['l','r','u','d'],repeat=no_of_moves)):
            temp_grid = copy.deepcopy(que_grid)
            for move in permutation:
                if move == 'l':
	            moveLeft(temp_grid)
	        elif move == 'r':
                     moveRight(temp_grid)
	        elif move == 'u':
	            moveUp(temp_grid)
	        else:
	            moveDown(temp_grid)
	    if temp_grid == ans_grid:
	        return permutation

def try_permutation(tmp_grid,permutation):
    print 'Initial'
    print tmp_grid
    for move in permutation:
        if move == 'l':
            print 'Moving Left'
            tmp_grid = moveLeft(tmp_grid)
            print tmp_grid
        elif move == 'r':
            print 'Moving Right'
            tmp_grid = moveRight(tmp_grid)
            print tmp_grid
        elif move == 'u':
            print 'Moving Up'
            tmp_grid = moveUp(tmp_grid)
            print tmp_grid
        else:
            print 'Moving Down'
            tmp_grid = moveDown(tmp_grid)
            print tmp_grid

def print_problem(q,a):
    print q, a

if __name__ == "__main__":
    que_grid = [] #[[0 for x in range(grid_size)] for x in range(grid_size)]
    ans_grid = [] #[[0 for x in range(grid_size)] for x in range(grid_size)]
    que_grid, ans_grid = parseImage('main.png',3)
    print_problem(que_grid,ans_grid)
    solution = solve(que_grid,ans_grid)
    solution = ''.join(solution)
    os.system('echo ' + solution + ' > solution')
