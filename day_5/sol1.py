import numpy as np
f = open("input.txt").read()

rnge, ids = f.split("\n\n")
rnge = rnge.split("\n")
ids = list(map(int,ids.split("\n")))

rtab = np.zeros((len(rnge),2),dtype=int)
for i,r in enumerate(rnge):
    rtab[i] = r.split("-")



fresh_count=0
for id in ids:
    for r in rtab:
        if r[0] <= id <= r[1]:
            fresh_count += 1
            break
print(fresh_count)