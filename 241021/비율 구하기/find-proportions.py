from sortedcontainers import SortedDict
n = int(input())

d = SortedDict()
for _ in range(n):
    color = input()
    if color in d:
        d[color] += 1
    else:
        d[color] = 1

for k in d.keys():
    print(f"{k} {d[k]/sum(d.values()) * 100}")