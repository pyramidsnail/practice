n = int(raw_input())

#def isprime(n):
def isprime(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return 0
        i+=2
    return 1


for i in xrange(4,n):
    if (not isprime(i)) and (not isprime(n-i)):
        print str(i)+' '+str(n-i)
        break

    
