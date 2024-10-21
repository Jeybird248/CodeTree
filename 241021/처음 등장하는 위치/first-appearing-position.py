from sortedcontainers import SortedDict
n = int(input())

arr = list(map(int, input().split()))

d = SortedDict()

for i, num in enumerate(arr):
    if num not in d:
        d[num] = i

for num in d.keys():
    print(f"{num} {d[num] + 1}")