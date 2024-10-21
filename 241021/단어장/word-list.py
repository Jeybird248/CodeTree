from sortedcontainers import SortedDict

n = int(input())

d = SortedDict()

for _ in range(n):
    word = input()
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

for num in d.keys():
    print(f"{num} {d[num]}")