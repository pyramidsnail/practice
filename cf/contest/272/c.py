a,b = map(int , raw_input().split())

total = 0

for i in xrange(1,b):
    for k in xrange(1,a+1):
        total += (k*i)*b+i

print total%1000000007
