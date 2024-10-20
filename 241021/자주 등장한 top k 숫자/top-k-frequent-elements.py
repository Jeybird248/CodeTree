n, k = map(int, input().split())
arr = list(map(int, input().split()))

d = {}
for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

top_k = sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)[:k]
for num in top_k:
    print(num[0], end = " ")