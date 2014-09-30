line = int(raw_input())
board = [['.' for x in xrange(line)]for x in xrange(line)]
for i  in xrange(line):
    temp = raw_input().strip()
    for j in xrange(line):
        board[i][j]= temp[j]

flag='YES'
for i in xrange(line):
    for j in xrange(line):
        count = 0
        if i-1>=0:
            if board[i-1][j]=='o':
                count += 1
        if j+1<line:
            if board[i][j+1]=='o':
                count += 1
        if i+1<line:
            if board[i+1][j]=='o':
                count += 1
        if j-1>=0:
            if board[i][j-1]=='o':
                count += 1

        if count%2==1:
            flag='NO'
            break

    if flag=='NO':
        break
print flag
            
            

