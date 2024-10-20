n = int(input())
A, B, C, D = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))

d = {}
for i in A:
    for j in B:
        if i + j in d:
            d[i + j] += 1
        else:
            d[i + j] = 1

count = 0
for i in C:
    for j in D:
        if 0 - i - j in d:
            count += d[0 - i - j]

print(count)