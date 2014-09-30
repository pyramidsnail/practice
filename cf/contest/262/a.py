n, m = map(int, raw_input().split())

count = n
day = 1
while count:
    count -=1
    if day%m==0:
        count += 1
    day += 1

print day-1
    
