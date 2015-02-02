[n, k] = [int(x) for x in raw_input().split()]
days = [int(x) for x in raw_input().split()]

if k<min(days):
    print 0
else:
    a = sorted(days)
    total=0
    time = k
    res = []
    for i in xrange(len(a)):
        if time - a[i] >= 0:
            res.append(days.index(a[i])+1)
            days[days.index(a[i])]=100000000
            time -= a[i]
            total += 1
        else:
            break
    print total
    for i in res:
        print i,
