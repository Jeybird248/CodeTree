from sortedcontainers import SortedSet
n, m = map(int, input().split())
s = SortedSet()

for _ in range(n):
    x, y = map(int, input().split())
    s.add((x, y))

for _ in range(m):
    x, y = map(int, input().split())
    index = s.bisect_left((x, y))
    if index < len(s):
        print(s[index][0], s[index][1])
    else:
        print(-1, -1)