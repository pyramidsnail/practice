def palindrome(string):
    flag=True
    for i in xrange(len(string)/2):
        if not string[i]==string[len(string)-1-i]:
            flag=False
            break
    return flag

t=int(raw_input())
for x in xrange(t):
    string=raw_input().strip()
    ans = 'NO'
    if  palindrome(string[1:]):
        ans = 'YES'
    if  palindrome(string[:len(string)-1]):
        ans = 'YES'
    for i in xrange(1,len(string)-1):
        new_string = string[:i]+string[i+1:]
        if  palindrome(new_string):
            ans = 'YES'
            break
    print ans
    
