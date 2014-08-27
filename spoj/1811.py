x=raw_input().strip()
y=raw_input().strip()
dp=[[0 for x in xrange(260000)]for x in xrange(260000)]

def lcs(x,y):
    for i in xrange(len(x)+1):
        for j in xrange(len(y)+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                 dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(x)][len(y)]


print lcs(x,y)
