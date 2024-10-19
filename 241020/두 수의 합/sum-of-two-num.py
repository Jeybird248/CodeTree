n, k = map(int, input().split())

arr = list(map(int, input().split()))

d = {}
count = 0

for num in arr:
    complement = k - num
    count += d.get(complement, 0)
    d[num] = d.get(num, 0) + 1

print(count)