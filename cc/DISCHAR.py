t=int(raw_input())

for i in xrange(t):
    string = raw_input().strip()
    dic = {}
    for j in string:
        if not j in dic:
            dic[j]=1
    print str(len(dic))
    
