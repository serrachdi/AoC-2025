import numpy as np

f = open("input.txt").read().splitlines()
count=0

def findmax(x):
    ind = np.argwhere(x == np.max(x))[0][0]
    return int(ind)

num = np.logspace(0,11,12)[::-1]
battery = np.zeros(12)
for line in f:
    line = [int(n) for  n in line]
    l = len(line)
    a = 0
    for i in range(12):
        if i != 11:
            linesearch = line[a:-(12 - i)+1]
        else:
            linesearch = line[a:]

        b = findmax(linesearch)
        a += b + 1
        battery[i] = linesearch[b]

    voltage = int(np.sum(num*battery))
    count += voltage

print(count)