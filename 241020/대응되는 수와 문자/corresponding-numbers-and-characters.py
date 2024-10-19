n, m = map(int, input().split())
d = {}
for i in range(1, n + 1):
    char = input()
    d[char] = str(i)
    d[str(i)] = char

for i in range(m):
    print(d[input()])