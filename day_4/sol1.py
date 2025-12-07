import numpy as np
f = open("input.txt").read().splitlines()

l = len(f)
tab = np.zeros((l+2,l+2)) # Padding with zeros to deal with edges

# Converting "@" and "." into 1s and 0s
for i,line in enumerate(f):
    tab[i+1,1:-1] = np.where(np.array(list(line)) == '@',1,0)
    

# Sum the surrounding
comp = tab[:-2,:-2] + tab[:-2,1:-1] + tab[:-2,2:] + tab[2:,:-2] + tab[2:,1:-1] + tab[2:,2:] + tab[1:-1,:-2] + tab[1:-1,2:]

final_diagram = (comp <4 ) & (tab[1:-1,1:-1] == 1)

print(np.sum(final_diagram))

