n = int(raw_input())

def getNumberCards(f):
    return 3*f*(f+1)/2-f

l = 0
h = 10000000

while l+1<h:
    m = (l+h)/2
    if getNumberCards(m)>n:
        h = m
    else:
        l = m
total = 0
while l:
    if (n+l)%3==0:
        total += 1
    l -= 1


print total
