string = raw_input()
while string!="0":
    mean = [-1 for x in xrange(6000)]
    mean[0] = 1

    for i in xrange(1,len(string)):
        if string[i]!='0':
            mean[i]=mean[i-1]
        if int(string[i-1:i+1])<27 and int(string[i-1:i+1])>9:
            mean[i]+=mean[0 if i-2<0 else i-2]
        # if string[i]=='0':
        #     if i>1 and i!=len(string)-1: 
        #         mean[i]=mean[i-2]
        #     elif i>1 and i==len(string-1):
        #         mean[i]=0
        #     else:
        #         mean[i]=1
        # elif int(string[i-1:i+1])>26:
        #     mean[i] = mean[i-1]
        # elif string[i-1]!='0':
            
        #     if int(string[i-1:i+1])>0 and int(string[i-1:i+1])<27 and i>1:
        #         mean[i]=mean[i-1]+mean[i-2]
        #     elif int(string[i-1:i+1])>0 and int(string[i-1:i+1])<27 and i<2:
        #         mean[i]=mean[i-1]+1
        # elif string[i-1]=='0':
        #     mean[i]=mean[i-1]
    print mean[len(string)-1]
    string=raw_input()
    
