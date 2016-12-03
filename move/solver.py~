import copy,os
from itertools import product
from PIL import Image

# getQueValue and getAnsValue depends on resolution of phone
def getQueValue(pixel):
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

def move(grid, dir):
    temp_grid = copy.deepcopy(grid)
    if dir == 'l':
        valid=moveLeft(temp_grid)
    elif dir == 'r':
        valid=moveRight(temp_grid)
    elif dir == 'u':
        valid=moveUp(temp_grid)
    else:
        valid=moveDown(temp_grid)
    return valid, temp_grid

def reverse(lm):
    if lm == 'l':
        return 'r'
    elif lm == 'r':
        return 'l'
    elif lm == 'u':
        return 'd'
    elif lm == 'd':
        return 'u'
    return 'n'

possible_moves={'l', 'r', 'u', 'd'}
que_grid = [] #[[0 for x in range(grid_size)] for x in range(grid_size)]

class solutions: sol=[]

def get_solution():
    return min(solutions.sol, key=len)

def solve(curr_grid,moves,last_move,depth,ans):
    global solution
    if depth>10:
        return

    moves+=last_move
    if(curr_grid==ans):
        solutions.sol.append(moves)
        return

    valid_moves=[]

    for m in possible_moves:
        if m!=reverse(last_move):
            valid, next_grid = move(curr_grid, m)
            if valid:
                valid_moves+=m

    for m in valid_moves:
        mc = copy.deepcopy(moves)
        valid, next_grid = move(curr_grid, m)
        solve(next_grid, mc, m, depth+1,ans)

def print_problem(q,a):
    print q, a

if __name__ == "__main__":
    ans_grid = [] #[[0 for x in range(grid_size)] for x in range(grid_size)]
    que_grid, ans_grid = parseImage('main.png',3)
    print_problem(que_grid,ans_grid)
    solve(que_grid,[],'n',1,ans_grid)
    s = get_solution()
    s=s[1:]
    s = ''.join(s)
    os.system('echo ' + s + ' > solution')
