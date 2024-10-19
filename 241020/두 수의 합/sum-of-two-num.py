n, k = map(int, input().split())

arr = list(map(int, input().split()))

d = {}
count = 0

for i in arr:
    if k - i in d:
        count += 1
    d[i] = k - i

print(count)