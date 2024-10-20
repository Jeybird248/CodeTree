n, k = map(int, input().split())

arr = list(map(int, input().split()))

count = 0
d = {}
for i in range(n):
    target = k - arr[i]
    seen = set()

    for j in range(i + 1, n):
        complement = target - arr[j]
        if complement in seen:
            count += 1
        seen.add(arr[j])

print(count)