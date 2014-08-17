import sys, re, os

cor=sys.stdin.readline()
cors = cor.split()
x1 = int(cors[0])
y1 = int(cors[1])
x2 = int(cors[2])
y2 = int(cors[3])

if (x1-x2)==0 and (y1-y2) != 0:
    edge = abs(y1-y2)
    print str(x1+edge)+' '+str(y1)+' '+str(x2+edge)+' '+str(y2)
elif (y1-y2) == 0 and (x1-x2) != 0:
    edge = abs(x1-x2)
    print str(x1)+' '+str(y1+edge)+' '+str(x2)+' '+str(y2+edge)

elif abs(x1-x2)==abs(y1-y2) and (y1-y2) != 0:
        print str(x1)+' '+str(y2)+' '+str(x2)+' '+str(y1)

else:
    print '-1'
