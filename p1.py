import os, sys

def sortCount(a,b):
    c=[]
    global inv
    i, j = 0, 0
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            inv += len(a)-i
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c
def divide(d):
    if len(d)>1:
        a = divide(d[0:int(len(d)/2)])
        b = divide(d[int(len(d)/2): len(d)])
        return sortCount(a,b)
    else:
        return d


inv = 0
array=[]
f=open('../IntegerArray.txt','r')
for i in f.readlines():
    array.append(int(i.strip()))
# array = [5,4,3,2,1]
sorted = divide(array)
print inv
