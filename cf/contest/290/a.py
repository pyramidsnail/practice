import sys, os, re

n, m = [int(x) for x in raw_input().split()]
for i in xrange(n):
    if i%2==0:
        for j in xrange(m):
            sys.stdout.write('#')
        sys.stdout.write('\n')
    elif (i/2)%2==1:
        sys.stdout.write('#')
        for j in xrange(1,m):
            sys.stdout.write('.')
        sys.stdout.write('\n')
    else:
        for j in xrange(m-1):
            sys.stdout.write('.')
        sys.stdout.write('#\n')
        
