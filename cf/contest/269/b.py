import itertools

n = int(raw_input())
diff = [int(x) for x in raw_input().split()]

vari = set(diff)
dic = {}
for i in vari:
    dic[i]=diff.count(i)
total = 1
for i in dic.keys():
    total *= dic[i]

if total >=n:
    print 'YES'
    ans = [[0 for x in xrange(4)] for x in range(n)]
    vari = sorted(vari, key=int)
    for i in vari:
        indx = [k for k, j in enumerate(diff) if j == vari[i]]
        temp = [x for x in itertools.permutations(indx)]
        for x in xrange(n):
            for y in xrange(vari.count(i)):
                ans[x][y] = temp[x%n][y]
for i in xrange(3):
    for j in xrange(n):
        if j!=n-1:
            print str(ans[i][j]+1)+' ',
        else:
            print str(ans[i][j])
            
    
        
        
    

else:
    print 'NO'
