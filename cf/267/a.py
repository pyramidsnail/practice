n = int(raw_input())

count = 0
for i in xrange(n):
    p, q = [int(x) for x in raw_input().split()]
    if q-p>=2:
        count += 1

print count
