import numpy as np

f = open("input.txt")
count=0

def findmax(x):
    a = np.argwhere(x == np.max(x))[0]
    return int(a)

for line in f:
    line = list(map(int,line[:-1]))
    
    a = findmax(line)
    if a == len(line) - 1:
        line2 = line[:a]
        b = findmax(line2)
        voltage = line[b]*10 + line[a]
        count += voltage
    else:
        line2 = line[a+1:]
        b = findmax(line2)
        voltage = line[a]*10 + line2[b]
        count += voltage

print(count)

