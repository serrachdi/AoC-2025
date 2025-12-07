import numpy as np

# Formating the input into a np array
f = open("input.txt")
content = f.read()
ls = content.split(",")
rnge = np.zeros((len(ls),2)).astype(int)
for i,x in enumerate(ls):
    rnge[i] = x.split('-')

# Checking the length of each ranges
# for _ in rnge:
#     #print(len(str(_[0])),"-",len(str(_[1])))
#     print(_[1]-_[0])
 
 
def hard_check(x):
    c = 0
    s_list=[]
    for _ in range(x[0],x[1]+1):
        _str = str(_)
        l = len(_str)
        if l%2 == 0:
            if _str[:int(l/2)] == _str[-int(l/2):]:
                c+=1
                s_list.append(_)


    return (c,s_list)


# np.set_printoptions(precision=0)
# i = -2
# print(rnge[i])
# print(hard_check(rnge[i]))

ijustwannasleepfckit = []
for lines in rnge:
    ijustwannasleepfckit += hard_check(lines)[1]
print(np.sum(ijustwannasleepfckit))