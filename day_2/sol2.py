import numpy as np

f = open("./input.txt")
content = f.read()
ls = content.split(",")
ran = []
# Separating ranges with different lengths
for x in ls:
    a = list(map(int,x.split('-')))
    b = a[:]
    if len(str(a[0])) != len(str(a[1])): # 45 - 335 will turns in 45 - 99 and 100 - 335
        a[1] = int(len(str(a[0]))*str(9))
        if len(str(a[0])) != 1: # Yeet the single digit ranges (yes talking to you 1-9)
            ran.append(a)
        b[0] = 10**len(str(a[0]))
        ran.append(b)
    else:
        if len(str(a[0])) != 1: # Same
            ran.append(a)


def get_chunk(l): # get what are the possible chunk sizes for a number of l digits
    chunk = []
    for i in range(2,l+1):
        if l%i == 0:
            chunk.append(l//i)
    return chunk


bad_id = []

for r in ran:
    l = len(str(r[0]))
    chunk = get_chunk(l)
    for ch in chunk:
        # bad_id = [] # To check what are the bad id for one given range and chunk size
        theoric_first_pos = int(str(r[0])[:ch]*int(l/ch))
        theoric_last_pos = int(str(r[1])[:ch]*int(l/ch))

        # Check first possible ?
        first_pos = r[0] <= theoric_first_pos and r[1] >= theoric_first_pos

        # Check last possible ?
        last_pos = r[1] >= theoric_last_pos and r[0] <= theoric_last_pos

        # Compute the npos, number of bad id in one range for a given chunk size 
        if ch == 1:
            npos = int(str(r[1])[0]) - int(str(r[0])[0])
        else:
            npos = int(str(r[1])[:ch]) - int(str(r[0])[:ch])

        if npos > 1:
            npos += first_pos + last_pos - 1
        elif npos ==1 :
            npos = first_pos + last_pos
        else:
            npos = int(last_pos)


        #Creating the bad id, starting from the first one of the range and iterating one by one up to npos
        if npos != 0:
            if first_pos:
                start = int(str(theoric_first_pos)[:ch])
            else:
                start = int(str(theoric_first_pos)[:ch]) + 1
            
            for i in range(npos):
                bad_id.append(int(str(start+i)*int(l/ch)))

        # print(r,ch,bad_id) # To check what are the bad id for one given range and chunk size
        
res = np.sum(np.unique(bad_id))
print(res)




