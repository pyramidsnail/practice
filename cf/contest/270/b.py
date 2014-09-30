n, k = [int(x)for x in raw_input().split()]
floor = [int(x)for x in raw_input().split()]

floor = sorted(floor)
total = 0
if k>=n:
    total = 2*(max(floor)-1)

else:
    temp = n%k
    while len(floor)>(k+temp):
        total += 2*(floor[k-1]-1)
        floor = floor[k:]
    total += 2*(floor[k-temp-1])
    total += 2*(floor[len(floor)-1]-1)

print total
