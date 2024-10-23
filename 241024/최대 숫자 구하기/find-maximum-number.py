from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = SortedSet([x for x in range(1, m + 1)])
for num in arr:
    if (1 <= num <= m):
        s.remove(num)
    print(s[-1])