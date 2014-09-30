a, b, c=map(int, raw_input().split())

def s(x):
    total = 0
    while x:
        total += x%10
        x = x/10

    return total


count = 0
solution = []
for i in xrange(1,73):
    if b*(i**a)+c<1000000000 and b*(i**a)+c>0:
        x = b*(i**a)+c
        if i==s(x):
            count += 1
            solution.append(b*i**a+c)



print count
solution.sort()
if count:
    for i in solution:
        print i,

