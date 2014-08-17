import sys
sys.setrecursionlimit(100000)

num = open("QuickSort.txt")
list = []
for i in num.readlines():
    list.append(int(i.strip()))

comp = 0
def choosepivot(a, rule):
    if rule==1:
        return 0
    if rule==2:
        return len(a)-1
    if rule==3:
        if len(a)%2 == 0:
            middle = len(a)/2-1
        else:
            middle = (len(a)-1)/2
        tmp = [a[0], a[middle], a[len(a)-1]]
        tmp = sorted(tmp)
        if tmp.index(a[0])==1:
            return 0
        if tmp.index(a[len(a)-1])==1:
            return len(a)-1
        else:
            return middle
            

def partition(a, rule):
    global comp
    if len(a)==1:
        return a
    else:
        i = 1
        j = 1
        # move the pivot to the first place
        index = choosepivot(a, rule)
        inter = a[index]
        a[index] = a[0]
        a[0] = inter
        while j<len(a):
            if a[j] < a[0]:
                inter = a[j]
                a[j] = a[i]
                a[i] = inter
                j += 1
                i += 1
                comp += 1
            else:
                j += 1
                comp += 1
        
            
        inter = a[i-1]
        a[i-1] = a[0]
        a[0] = inter
        if i==1:
            partition(a[i:len(a)], rule)
        elif i==len(a):
            partition(a[0:i-1], rule)            
        else:
            partition(a[0:i-1], rule)
            partition(a[i:len(a)], rule)

b = partition(list,3)
print comp
