def f(n):
    if n==1:
        return 1
    else:
        return f(n-1)*(n**n)

t = int(raw_input())
for i in xrange(t):
    n,m,q = [int(x) for x in raw_input().split()]
    for j in xrange(q):
        r = int(raw_input())
        max_value = max(r, n-r)
        min_value = min(r, n-r)
        tmp1 = 1
        for x in xrange(max_value+1, n+1):
            tmp1 *= x**x
        print (tmp1/f(min_value))%m
        
