import numpy as np
f = open("input.txt")

dial = 50
count0 = 0
for x in f:
    mv = int(x[1:])

    if x[0] == 'L':
        mv *= -1
    res = dial + mv

    if res <=0 and dial !=0:
        count0+=1
    count0 += abs(res)//100

    dial = res % 100
print(count0)