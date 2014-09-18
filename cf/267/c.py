m = int(raw_input())
items = raw_input().split()

n=int(raw_input())
dic = {}
for i in xrange(n):
    s1, s2 = raw_input().split()
    if s1.lower() not in dic:
        dic[s1.lower()]=s2.lower()
    else:
        if s2.lower().count('r')<dic[s1.lower()].count('r'):
            dic[s1.lower()]=s2.lower()
        elif len(s2)<len(dic[s1.lower()]):
            dic[s1.lower()]=s2.lower()

num_r = 0
length = 0

for i in len(items):
    if items[i].lower() in dic.keys():
        if items[i].lower().count('r')>dic[items[i].lower()].count('r'):
            num_r += dic[items[i].lower()].count('r')
            length += len(dic[items[i].lower()])
            items[i]=dic[items[i].lower()]
        elif len(items[i])>len(dic[items[i].lower()]):
            num_r += dic[items[i].lower()].count('r')
            length += len(dic[items[i].lower()])
            items[i]=dic[items[i].lower()]lower()]

    else:
        num_r += items[i].lower().count('r')
        length += len(items[i])

print num_r, length


