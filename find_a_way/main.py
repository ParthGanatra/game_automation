from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os, time

# Dependent on device
red = (-1, 254, 76, 101)
grey = (-1, 204, 204, 204)
black = (-1, 0, 0, 0)
white = (-1, 255, 255, 255)
step = 140
start_x = 535
start_y = 180
no_x = 6
no_y = 8

device = MonkeyRunner.waitForConnection()
print("device connected")

def get_problem():
    image = device.takeSnapshot()
    f = open('que', 'w')
    f.write(str(no_y) + " " + str(no_x) + "\n")
    t_i = 0
    t_j = 0
    count=0
    for j in range(no_y):
        for i in range(no_x):
            pixel = image.getRawPixel(start_y + step*i, start_x + step*j)
            if pixel == red:
                initial = (start_y + step*i, start_x + step*j)
                t_i = i
                t_j = j
                f.write("1 ")
            elif pixel == black:
                count+=1
                f.write("-1 ")
            else:
                f.write("0 ")
        f.write("\n")
    f.write(str(t_j) + " " + str(t_i) + " " + str(no_y*no_x - count) + "\n")
    f.close()
    return initial

def solve_problem(initial, solution):
    for sol in solution:
        if sol == "1":
            nxt = (initial[0], initial[1] - step)
        elif sol == "0":
            nxt = (initial[0], initial[1] + step)
        elif sol == "2":
            nxt = (initial[0] - step,initial[1])
        else:
            nxt = (initial[0] + step,initial[1])
        device.drag(initial, nxt, 0.05)
        initial = nxt

#UP:1, DOWN:0, LEFT:2, RIGHT:3
def solve_level():
    initial = get_problem()
    os.system("./solver")
    fo = open("ans", "r")
    sol = fo.readline().split()
    solve_problem(initial, sol)
    time.sleep(1)
    device.touch(540,760,MonkeyDevice.DOWN_AND_UP)

for i in range(10):
    solve_level()
    time.sleep(1.5)
