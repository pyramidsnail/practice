import sys, os, re

n, m = [int(x) for x in raw_input().split()]
array = [['A' for x in range(m)] for x in range(n)]
for i in xrange(n):
    array[i] = raw_input().strip().split('')

dic = {}
for i in xrange(n):
    for j in xrange(m):
        count = 0
        if i-1>=0 and array[i-1][j] == array[i][j]:
            count += 1
        if i+1<n and array[i+1][j] == array[i][j]:
            count += 1
        if j-1>0 and array[i][j-1] == array[i][j]:
            count += 1
        if j+1<m and array[i][j+1] == array[i][j]:
            count += 1
        if count > 1:
            if array[i][j] in dic:
                dic[array[i][j]].append((i,j))
            else:
                dic[array[i][j]] = [(i,j)]

