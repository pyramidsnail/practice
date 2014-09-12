x=raw_input().strip()
y=raw_input().strip()
max_length = max(len(x), len(y))+10
dp=[[0 for z in xrange(max_length)]for z in xrange(max_length)]

# def lcs(x,y):
#     for i in xrange(len(x)+1):
#         for j in xrange(len(y)+1):
#             if i==0 or j==0:
#                 dp[i][j]=0
#             elif x[i-1]==y[j-1]:
#                  dp[i][j]=dp[i-1][j-1]+1
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#     return dp[len(x)][len(y)]


# print lcs(x,y)



def lcs(x,y):
    result = 0
    for i in xrange(len(x)+1):
        for j in xrange(len(y)+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                 dp[i][j]=dp[i-1][j-1]+1
                 result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result


print lcs(x,y)
