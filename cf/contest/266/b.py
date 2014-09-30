n, a, b = [int(x) for x in raw_input().split()]

if a*b>=6*n:
    print a*b
    print str(a)+' '+str(b)
else:
    if (6*n)%a==0:
        room=6*n
        b = (6*n)/a
    elif (6*n)%b==0:
        room = 6*n
        a = (6*n)/b
    else:
        flag=False
        for j in xrange(6*n,6000000000):
            for i in xrange(min(a,b), j/min(a,b)+1):
                if j%i==0 and j/i>max(a,b):
                    room = j
                    flag=True
                    if i>=a and j/i>=b:
                        a=i
                        b=j/i
                    else:
                        a=j/i
                        b=i
                    break
            if flag==True:
                break
        
    print room
    print str(a)+' '+str(b)
            
        
    
    
        
