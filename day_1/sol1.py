import numpy as np
f = open("input.txt")

dial = 50
count0 = 0
for x in f:
    mv = int(x[1:])
    if x[0] == 'L':
        mv *= -1
    res = dial + mv
    dial = res % 100
    if dial ==0:
        count0 += 1
print(count0)