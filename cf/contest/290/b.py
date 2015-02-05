import sys, os, re

visited = []
def dfs(start, graph):
    visited.append(start)
    (a,b) = start
    if (a-1, b) in graph and (a-1, b) not in visited:
        return dfs((a-1,b), graph)
    elif (a-1, b) in graph  and (a-1, b) in visited and visited.index((a-1,b))!=len(visited)-2:
        return True

    
    elif (a+1, b) in graph and (a+1, b) not in visited:
        return dfs((a+1,b), graph)
    elif (a+1, b) in graph  and (a+1, b) in visited and visited.index((a+1,b))!=len(visited)-2:
        return True

    elif (a, b-1) in graph and (a, b-1) not in visited:
        return dfs((a,b-1), graph)
    elif (a, b-1) in graph  and (a, b-1) in visited and visited.index((a,b-1))!=len(visited)-2:
        return True
    
    elif (a, b+1) in graph and (a, b+1) not in visited:
        return dfs((a,b+1), graph)
    elif (a, b+1) in graph  and (a, b+1) in visited and visited.index((a,b+1))!=len(visited)-2:
        return True

    return False
    
        
    
    
        

n, m = [int(x) for x in raw_input().split()]
array = [[] for x in range(n)]
for i in xrange(n):
    array[i] += raw_input().strip()

dic = {}
for i in xrange(n):
    for j in xrange(m):
        # count = 0
        # if i-1>=0 and array[i-1][j] == array[i][j]:
        #     count += 1
        # if i+1<n and array[i+1][j] == array[i][j]:
        #     count += 1
        # if j-1>0 and array[i][j-1] == array[i][j]:
        #     count += 1
        # if j+1<m and array[i][j+1] == array[i][j]:
        #     count += 1
        # if count > 1:
        if array[i][j] in dic:
            dic[array[i][j]].append((i,j))
        else:
            dic[array[i][j]] = [(i,j)]
flag = 0
for i in dic:
    for j in dic[i]:
        visited = []
        if dfs(j, dic[i]):
            print 'Yes'
            flag = 1
            break
    if flag:
        break
if not flag:
    print 'No'
        

