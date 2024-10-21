n = int(input())
d = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x in d:
        d[x] = min(y, d[x])
    else:
        d[x] = y
s = 0
for x in d:
    s += d[x]

print(s)