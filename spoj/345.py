n = int(raw_input())
colors = [int(x) for x in raw_input().split()]
dp = [[-1 for x in xrange(100)] for x in xrange(100)]
def mix(a,b):
    total = 0
    for i in xrange(a-1,b):
        total += colors[i]
    return total%100

def solve(a,b):
    if dp[a][b]!=-1:
        return dp[a][b]
    

    if a==b:
        return 0
    # elif a+1==b:
    #     dp[a][b] = colors[a-1]*colors[b-1]
    #     return dp[a][b]
    else:
        for i in xrange(a,b+1):
            temp=solve(a,i)+solve(i+1,b)+mix(a,i)*mix(i+1,b)
            if dp[a][b] ==-1:
                dp[a][b]=temp
            else:
                dp[a][b]=min(dp[a][b],temp )
    return dp[a][b]

print solve(1,n)






