class TaroGrid:
    def getNumber(self, grid):
        longest = 0
        for i in xrange(len(grid)):
            temp = 1
            for j in xrange(len(grid)):
                if j<len(grid)-1 and grid[i][j-1]==grid[i][j]:
                    temp += 1
                else:
                    temp = 1
                    
            if temp> longest:
                longest=temp
        return longest
