from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os,sys,time

device = MonkeyRunner.waitForConnection()
print 'Device Connected'
def swipeLeft():
    #print 'Left Swipe'
    device.drag((900,900),(200,900),0.5)

def swipeRight():
    #print 'Right Swipe'
    device.drag((200,900),(900,900),0.5)

def swipeDown():
    #print 'Down Swipe'
    device.drag((500,300),(500,900),0.5)

def swipeUp():
    #print 'Up swipe'
    device.drag((500,900),(500,300),0.5)

def solveLevel():
    scrshot = device.takeSnapshot()
    scrshot.writeToFile('main.png','png')
    print "Solving"
    os.system('python solver.py')
    print "Solved"
    sol = open('solution','r')
    sol = list(sol.readline())
    sol.pop()
    print sol
    for swipe in sol:
        time.sleep(0.5)
        if swipe == 'l':
            swipeLeft()
        elif swipe == 'r':
            swipeRight()
        elif swipe == 'd':
            swipeDown()
        elif swipe == 'u':
            swipeUp()
        else:
            print error
    time.sleep(1)

if __name__ == '__main__':
    levels = int(sys.argv[1])
    for i in range(levels):
        print 'Next Level'
        solveLevel()
        device.touch(670,890,MonkeyDevice.DOWN_AND_UP)
        time.sleep(2)
