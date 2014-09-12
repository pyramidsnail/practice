n = int(raw_input())
arr = [int(x) for x in raw_input().split()]

num=0

for i in xrange(1,len(arr)-2):
    for j in xrange(i+1,len(arr)):
        if sum(arr[0:i])==sum(arr[i:j]) and sum(arr[i:j])==sum(arr[j:]):
            num +=1

print num
