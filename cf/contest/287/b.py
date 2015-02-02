[r,x0,y0,x1,y1] = [int(x) for x in raw_input().split()]

if x0==x1 and y0==y1:
    print 0
else:
    total = 0
    total += abs(x0-x1)/(2*r) + abs(y0-y1)/(2*r)
    if abs(x0-x1)%(2*r)==0 and abs(y0-y1)%(2*r)==0:
        pass

    elif abs(x0-x1)%(2*r)<=r and abs(y0-y1)%(2*r)<=r:
        total += 1
    # elif abs(x0-x1)%(2*r)>r and abs(y0-y1)%(2*r)>r:
    #     total += 2

    else:
        total += 2
    print total
    
    
