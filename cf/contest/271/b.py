n = int(raw_input())
a = map(int, raw_input().split())
m = int(raw_input())
q = map(int, raw_input().split())

border = [a[0]]
for i in xrange(1,n):
    border.append(border[i-1]+a[i])

for i in xrange(m):
    if q[i]<= border[0]:
        print '1'
    elif q[i]>border[-2]:
        print str(n)
    else:
        l = 0
        h = len(border)
        m = (l+h)/2
        while l+1<h:
            if q[i]>border[m]:
                l = m
                m = (l+h)/2
            elif q[i]<border[m]:
                h=m
                m = (l+h)/2
            else:
                l = m-1
                break
        print str(l+2)
        # for j in xrange(1,len(border)):
        #     if q[i]>border[j] and q[i]<=border[j+1]:
        #         print str(j+2)
        
