test = int(raw_input())
girl = [int(x) for x in raw_input().split()]
girl = girl[0:-1]
line=raw_input()
dp=[[0 for x in xrange(2100)] for x in xrange(2100) ]

def LCS(girl, boy, m, n):
    
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif boy[j-1]==girl[i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] =max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]


while test:
    test -=1
    score = 0
    while True:
        if line.startswith('0'):
            break
        
        boy = [int(x) for x in line.split()]
        boy = boy[0:-1]
        dp=[[0 for x in xrange(2100)] for x in xrange(2100)]
        score = max(score, LCS(girl, boy, len(girl), len(boy)))
        line=raw_input()
    line=raw_input()
        
    print score
