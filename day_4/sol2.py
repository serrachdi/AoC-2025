import numpy as np
f = open("input.txt").read().splitlines()

l = len(f)
tab = np.zeros((l+2,l+2)) # Padding with zeros to deal with edges

# Converting "@" and "." into 1s and 0s
for i,line in enumerate(f):
    tab[i+1,1:-1] = np.where(np.array(list(line)) == '@',1,0)
    

# Sum the surrounding
def get_surrounding(x):
    return x[:-2,:-2] + x[:-2,1:-1] + x[:-2,2:] + x[2:,:-2] + x[2:,1:-1] + x[2:,2:] + x[1:-1,:-2] + x[1:-1,2:]

def get_removed_rolls(x):
    return (get_surrounding(x) < 4) & (x[1:-1,1:-1] == 1)

total_removed = 0
roll_removed = 1

while roll_removed != 0:
    next_diag = get_removed_rolls(tab)
    tab[1:-1,1:-1] -= next_diag
    roll_removed = np.sum(next_diag)
    total_removed += roll_removed

print(total_removed)

