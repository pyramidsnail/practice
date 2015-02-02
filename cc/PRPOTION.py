t = int(raw_input())

while t:
    r,g,b,m = map(int, raw_input().split())
    rl = sorted(map(int, raw_input().split()),reverse=True)
    gl = sorted(map(int,raw_input().split()),reverse=True)
    bl = sorted(map(int, raw_input().split()),reverse=True)
    while m:
        if rl[0]>=gl[0]and rl[0]>=bl[0]:
            for i in xrange(r):
                rl[i]=rl[i]/2
        elif bl[0]>=gl[0]and bl[0]>=rl[0]:
            for i in xrange(b):
                bl[i]=bl[i]/2
        else:
            for i in xrange(g):
                gl[i]=gl[i]/2
            
        m -=1
    print max([rl[0],bl[0],gl[0]])

    t -= 1

    
