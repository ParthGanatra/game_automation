from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
device = MonkeyRunner.waitForConnection()
print 'device Connected'


def calculateTime(distance):
    return distance/1062.00
    
def findRed():
    flag = -1
    result = device.takeSnapshot()
    start = 0
    cflag = False
    for i in range(3,1080):
        #print i,
        pixel = result.getRawPixel(i, 1365)
        if flag == -1 and pixel == (-1, 0, 0, 0):
            flag = 0
        elif flag == 0 and pixel != (-1, 0, 0, 0):
            flag = 1
            start = i
        elif flag == 1 and pixel == (-1, 0, 0, 0):
            #return i + 10 - start
            flag = 2
        elif flag == 2 and pixel == (-1, 247, 27, 27):
            print (i - start)
            return (i - start)

        if(not cflag and i%5==0):
            rpi = result.getRawPixel(i, 1415)
            if rpi == (-1, 225, 13, 13):
                for j in range(0,6):
                    if result.getRawPixel(i+j, 1415)!=(-1, 225, 13, 13):
                        continue
                print "Found cherry at " + str(i)
                cflag=True

for j in range(100):
    distance = findRed()
    t = calculateTime(distance)
    print distance, t
    device.drag((500,500),(500,500),t)
    time.sleep(0.2)
    if distance>300:
        device.touch(500, 500, MonkeyDevice.DOWN)
        time.sleep(0.3)
        device.touch(500, 500, MonkeyDevice.UP)
        time.sleep(0.3)
        device.touch(500, 500, MonkeyDevice.DOWN)
        time.sleep(0.3)
        device.touch(500, 500, MonkeyDevice.UP)
    time.sleep(3)
