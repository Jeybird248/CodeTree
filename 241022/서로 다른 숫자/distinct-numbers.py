n = int(input())
arr = list(map(int, input().split()))

d = set()
for num in arr:
    d.add(num)

print(len(d))