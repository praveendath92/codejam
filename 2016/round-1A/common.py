IN = open('data/data.in', 'r')
OUT = open('data/data.out', 'w')

def setInOut(src, dst):
    global IN
    global OUT
    IN.close()
    OUT.close()
    IN = open(src, 'r')
    OUT = open(dst, 'w')

def readLine():
    return IN.readline()

def readInt():
    return int(readLine())

def readIntArr():
    return [int(i) for i in readLine().split(' ')]

def readCharArr():
    return [i for i in readLine().split(' ')]

def write(data):
    OUT.write(data)

def writeLine(data):
    write(data + "\n")

def done():
    IN.close()
    OUT.close()

setInOut('data/C-large-practice.in','data/C-large-practice.out')
#setInOut('data/B-large-practice.in','data/B-large-practice.out')