direction = raw_input()
org = raw_input()

l1 = 'qwertyuiop'
l2 = 'asdfghjkl;'
l3 = 'zxcvbnm,./'

out = ''
for i in xrange(len(org)):
    if l1.find(org[i])!=-1:
        if direction == 'R':
            out += l1[l1.find(org[i])-1]
        else:
            out += l1[l1.find(org[i])+1]
    elif l2.find(org[i])!=-1:
        if direction == 'R':
            out += l2[l2.find(org[i])-1]
        else:
            out += l2[l2.find(org[i])+1]
    else:
        if direction == 'R':
            out += l3[l3.find(org[i])-1]
        else:
            out += l3[l3.find(org[i])+1]

print out

    
