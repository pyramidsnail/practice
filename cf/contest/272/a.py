n, m = map(int, raw_input().split())

if n<m:
    print -1
else:
    if n%2==0:
        minstep = n/2+(m-(n/2)%m)
    else:
        minstep = n/2+1+(m-((n/2)+1)%m)
    print minstep
