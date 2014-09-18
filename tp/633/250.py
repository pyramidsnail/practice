class Target:
    def draw(self,n):
        out = [[' ' for x in xrange(n)] for x in xrange(n)]
        for i in xrange(0,n/2+1,2):
            # for j in xrange(i,(n-i)):
            for k in xrange(i, (n-i)):
                out[i][k]='#'
                out[n-i-1][k]='#'
                out[k][i]='#'
                out[k][n-i-1]='#'
        new = []
        for i in xrange(n):
            temp = ''
            for j in xrange(n):
                temp+=out[i][j]
            new.append(temp)
        tuple(new)
        return new


if __name__ == '__main__':
    test = Target()
    re=test.draw(9)
            
