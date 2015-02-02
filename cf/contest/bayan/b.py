n, m = map(int, raw_input().split())
h = raw_input()
v = raw_input()

if (h[0]=='<'and v[0]=='^')or (h[-1]=='<'and v[0]=='v')\
   or (h[0]=='>'and v[-1]=='^')or(h[-1]=='>'and v[-1]=='v'):
    print 'NO'
else:
    print 'YES'
