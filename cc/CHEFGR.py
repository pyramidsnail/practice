t = int(raw_input())
while t:
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    total = sum(a)+m
    if total%n==0 and total/n>=max(a):
        print 'Yes'
    else:
        print 'No'
    t -= 1

