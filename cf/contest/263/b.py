from collections import Counter

n, k = [int(x) for x in raw_input().split()]
cards = list(raw_input().strip())

letter = dict((x,cards.count(x)) for x in set(cards))

re=Counter(letter).most_common()
score = 0
while k:
    i = 0
    if k>=re[i][1]:
        score += re[i][1]**2
        k -= re[i][1]
    else:
        score += k**2
        k=0
    i = i+1

print score
