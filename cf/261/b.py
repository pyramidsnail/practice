import sys, os, re

n = int(sys.stdin.readline())
case = sys.stdin.readline()
beauty = [int(x) for x in case.split()]

max_diff = 0
set = 0
for i in xrange(len(beauty)):
    for j in xrange(i+1,len(beauty)):
       if abs(beauty[i]-beauty[j])==max_diff:
           set += 1
       if abs(beauty[i]-beauty[j])>max_diff:
           max_diff = abs(beauty[i]-beauty[j])
           set = 1

print str(max_diff)+' '+str(set)
