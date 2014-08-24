# import algorithms


line = raw_input()
case = 0
while(line!='0'):
    ###  two strategies: keep old or fire extra
    case += 1
    items = [int(x)for x in line.split()]
    mon, hire, salary, severance = items[0:4]
    num = items[4:]
    # people = [0]*25
    # money = [0]*25
    # people[0]=num[0]
    money = [[float("inf") for x in xrange(25)]for x in xrange(300)]
    money[0][num[0]] = hire*num[0]+salary*num[0]
    for i in xrange(1,mon):
        for x in xrange(min(num),max(num)):
            for y in xrange(min(num),max(num)):
                if y>x:
                    money[i][y] = min(money[i][y]+,money[i-1][x] + hire*(y-x)+y*salary)
                else:
                    money[i][y] = min(money[i][y],money[i-1][x] +severance*(x-y) +y*salary)

        # if num[i]>people[i-1]:
        #     people[i]=num[i]
        #     money[i]=money[i-1]+hire*(num[i]-people[i-1])+people[i]*salary
        # else:
        #     min_money=float("inf")
        #     min_people = people[i-1]
        #     for j in xrange(num[i],min_people+1):
        #         temp = money[i-1]+severance*(people[i-1]-j)+j*salary
        #         if temp<min_money:
        #             money[i]=temp
        #             min_money=temp
        #             people[i] = j
            
            
            # change = money[i-1]+severance*(people[i-1]-num[i])+num[i]*salary
            # keep = money[i-1] + people[i-1]*salary
            # if change<keep:
            #     people[i] = num[i]
            #     money[i]=change
            # else:
            #     people[i]=people[i-1]
            #     money[i]=keep
                
    print "Case %d, cost = $%d" %(case,money[mon-1])
    line=raw_input()
    
