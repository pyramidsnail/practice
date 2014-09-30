items = [int(x) for x in raw_input().split()]

kinds = set(items)
flag=1
if len(kinds)==3:
    for i in kinds:
        if items.count(i)==4:
            print 'Bear'
            flag=0
            break
    if flag:
        print 'Alien'
    
elif len(kinds)==2:
    for i in kinds:
        if items.count(i)==4:
            print 'Elephant'
            flag=0
            break
    if flag:
        print 'Alien'

elif len(kinds)==1:
    print 'Elephant'
else:
    print 'Alien'
        
