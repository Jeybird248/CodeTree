n = int(input())
d = {}

maxCount, maxColor = 0, "None"

for i in range(n):
    color = input()
    if color not in d:
        d[color] = 1
    else:
        d[color] += 1
    if d[color] > maxCount:
        maxColor = color
        maxCount = d[color]

print(maxCount)