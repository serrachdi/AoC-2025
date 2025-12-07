import numpy as np
f = open("input.txt").read()

rnge = f.split("\n\n")[0].split("\n")

rtab = np.zeros((len(rnge),2),dtype=int)
for i,r in enumerate(rnge):
    rtab[i] = r.split("-")

cond = 1
t = np.copy(rtab)
while cond:
    
    for i,r in enumerate(t):
        a = r[0]
        b = r[1]

        check = (t[:,0] < a) & (t[:,1] > a) & (t[:,1] < b)
        if np.sum(check) != 0:
            t[check,1] = b
            t = np.delete(t,i,axis=0)
            break

        check2 = (t[:,0] < a) & (t[:,1] > b)
        if np.sum(check2) != 0:
            t = np.delete(t,i,axis=0)
            break

        check3 = (t[:,0] < a) & (t[:,1] == b)
        if np.sum(check3) != 0:
            t = np.delete(t,i,axis=0)
            break

        check4 = (t[:,0] == a) & (t[:,1] > b)
        if np.sum(check4) != 0:
            t = np.delete(t,i,axis=0)
            break

        check5 = (t[:,0] > a) & (t[:,0] == b) & (t[:,1] > b)
        if np.sum(check5) != 0:
            t[check5,0] = a 
            t = np.delete(t,i,axis=0)
            break

    stop = (np.sum(check) == 0) and (np.sum(check2) == 0) and (np.sum(check3) == 0) and (np.sum(check4) == 0) and (np.sum(check5) == 0)
    if stop:
        cond = 0
t = np.unique(t,axis=0)
res = np.sum(t[:,1] - t[:,0] + 1)
print(res)