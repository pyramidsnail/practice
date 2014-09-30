n,m,k = [int(x) for x in  raw_input().split()]
arr = [[0 for x in xrange(n)] for x in xrange(m+1)]

for i in xrange(m+1):
    x = int(raw_input())
    j = 0
    while x:
        arr[i][j]=x%2
        x=x/2
        j += 1

count = 0
for i in xrange(m-1, -1, -1):
    diff = 0
    for j in xrange(n):
        if arr[m][j] != arr[i][j]:
            diff += 1
            if diff > k:
                break

    if diff<=k:
        count += 1

print count
