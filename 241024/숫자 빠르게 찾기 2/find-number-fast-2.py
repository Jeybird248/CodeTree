from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = SortedSet(map(int, input().split()))

for _ in range(m):
    index = arr.bisect_right(int(input()) - 1)
    if index < len(arr):
        print(arr[index])
    else:
        print(-1)