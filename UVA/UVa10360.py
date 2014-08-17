import sys, re, os

sce = int(sys.stdin.readline())
for i in range(sce):
    d = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    x = []
    y = []
    size = []
    maxList=[0,0,0]
    for j in range(n):
        line = sys.stdin.readline()
        x.append(int(line.split()[0]))
        y.append(int(line.split()[1]))
        size.append(int(line.split()[2]))
    for m in range(min(x), max(x)):
        for n in range(min(y),max(y)):
            total = 0
            for r in range(len(x)):
                if not (abs(x[r]-m)>d or abs(y[r]-n)>d):
                    total += size[r]
            if total>maxList[2]:
                maxList[0]=m
                maxList[1]=n
                maxList[2]=total
    print str(maxList[0])+" "+str(maxList[1])+" "+str(maxList[2])
                    
