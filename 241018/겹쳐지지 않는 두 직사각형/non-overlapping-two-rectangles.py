n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        prefix[i][j] = grid[i][j]
        if i > 0:
            prefix[i][j] += prefix[i - 1][j]
        if j > 0:
            prefix[i][j] += prefix[i][j - 1]
        if i > 0 and j > 0:
            prefix[i][j] -= prefix[i - 1][j - 1]

def get_sum(x1, y1, x2, y2):
    result = prefix[x2][y2]
    if x1 > 0:
        result -= prefix[x1 - 1][y2]
    if y1 > 0:
        result -= prefix[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        result += prefix[x1 - 1][y1 - 1]
    return result

max_total_sum = float('-inf')

for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                sum1 = get_sum(x1, y1, x2, y2)
                
                for i1 in range(0, x1):
                    for j1 in range(m):
                        for i2 in range(i1, x1 - 1):
                            for j2 in range(j1, m):
                                sum2 = get_sum(i1, j1, i2, j2)
                                total_sum = sum1 + sum2
                                max_total_sum = max(max_total_sum, total_sum)

                for i1 in range(x2 + 1, n):
                    for j1 in range(m):
                        for i2 in range(i1, n): 
                            for j2 in range(j1, m):
                                sum2 = get_sum(i1, j1, i2, j2)
                                total_sum = sum1 + sum2
                                max_total_sum = max(max_total_sum, total_sum)

                for i1 in range(n):
                    for j1 in range(0, y1):
                        for i2 in range(i1, n):
                            for j2 in range(j1, y1 - 1): 
                                sum2 = get_sum(i1, j1, i2, j2)
                                total_sum = sum1 + sum2
                                max_total_sum = max(max_total_sum, total_sum)

                for i1 in range(n):
                    for j1 in range(y2 + 1, m):
                        for i2 in range(i1, n):
                            for j2 in range(j1, m):
                                sum2 = get_sum(i1, j1, i2, j2)
                                total_sum = sum1 + sum2
                                max_total_sum = max(max_total_sum, total_sum)
print(max_total_sum)