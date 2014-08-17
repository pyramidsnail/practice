from itertools import product


n, k, d = map(int, raw_input().split())
# for roll in product([1,2,3,4], repeat=2):
#     print roll

if k**d<n:
    print '-1'
    
else:
    cols =  list(product(xrange(1,k+1), repeat=d))
    
    for i in range(d):
        for j in xrange(n):
            print cols[j][i],
        print '\n'
            
        
