n = int(input()) 
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))  
    matrix.append(row)

def count(x, y):
    counter = 0
    for i in range(3):
        for j in range(3):
            if 0 <= x + i < n and 0 <= y + j < n and matrix[y + j][x + i] == 1:
                counter += 1
    return counter

maxCount = 0
for i in range(n):
    for j in range(n):
        maxCount = max(maxCount, count(i, j))

print(maxCount)