n = int(raw_input())

print '+------------------------+'
lst1=['#']*11
lst2=['#']*11
lst4=['#']*11
third = '#'
if n >2:
    third = 'O'


if n>3:
    lst4[0]='O'
if n>1:
    lst2[0]='O'
if n>0:
    lst1[0]='O'
if n>4:
    resi = (n-4)%3
    row = (n-4)/3
    if resi >1:
        lst2[row+1]='O'
    if resi >0:
        lst1[row+1]='O'
    for i in xrange(1,row+1):
        lst1[i]='O'
        lst2[i]='O'
        lst4[i]='O'
# print '|'+".".join(lst1)+'.|D|)'
# print '|'+ ".".join(lst2)+'.|.|'
# print '|'+third+'.......................|'
# print '|'+".".join(lst4)+'.|.|)'
# print '+------------------------+'

print '|'+".".join(lst1)+'.|D|)\n'+'|'+ ".".join(lst2)+'.|.|\n'+\
      '|'+third+'.......................|\n'+\
      '|'+".".join(lst4)+'.|.|)\n'+\
      '+------------------------+'





    
