import math

n = int(raw_input())
data =[int(x)for x in raw_input().split()]
score = sum(data)

tie = int(math.log2(len(data)))
score += tie*sum(data)

if len(data)-2**tie==1:
    score += sum(data)-min(data)
# else:
#     score += sum(data)

print data

# def big(data):
#     if len(data)==1:
#         return score
#     else:
        
