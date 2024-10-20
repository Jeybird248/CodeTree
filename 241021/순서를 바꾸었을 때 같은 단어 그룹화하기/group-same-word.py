n = int(input())
d = {}
biggestCount = 0
for i in range(n):
    word = ''.join(sorted(input()))
    if word in d:
        d[word] += 1
        biggestCount = max(biggestCount, d[word])
    else:
        d[word] = 1
print(biggestCount)