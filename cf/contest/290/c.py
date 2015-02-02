import sys, re, os

lexi = ''
flag = 1
n = int(raw_input())
lines = []
for i in xrange(n):
    lines.append(raw_input().strip())
ref = lines[0]
for i in xrange(1,n):
    then = lines[i]
    for j in xrange(min(len(ref),len(then))):
        if ref[j] != then[j]:
            if not then[j] in lexi:
                if ref[j] in lexi:
                    lexi += then[j]
                else:
                    lexi += ref[j]
                    lexi += then[j]
                ref = then
            else:
                if lexi.index(ref[j])>lexi.index(then[j]):
                    flag = 0
                else:
                    ref = then
            break
    if not flag:
        break

if not flag:
    print 'Impossible'
else:
    table = 'abcdefghijklmnopqrstuvwxyz'
    for i in table:
        if not i in lexi:
            lexi += i
    print lexi
