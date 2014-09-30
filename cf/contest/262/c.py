from operator import itemgetter
# min(enumerate(a), key=itemgetter(1))[0] 

n, m, w = map(int, raw_input().split())
height = map(int, raw_input().split())

while m:
    indx = min(enumerate(height), key=itemgetter(1))[0]
    if len(height)>= indx + w +1:
        for i in xrange(w):
            height[indx+i] += 1
    else:
        for i in xrange(len(height)-w,len(height)):
            height[i] += 1

    m -=1


print min(height)
