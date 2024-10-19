n, m = map(int, input().split())
arr = list(map(int, input().split()))
numbers = list(map(int, input().split()))
d = {}
for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
for num in numbers:
    if num in d:
        print(d[num], end = " ")
    else:
        print(0, end = " ")