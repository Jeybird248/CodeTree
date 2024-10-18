n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_sum = float('-inf') 
def get_diagonal_sum(x1, y1, x2, y2):
    dx = 1 if x2 > x1 else -1  
    dy = 1 if y2 > y1 else -1  

    diagonal_sum = 0
    x, y = x1, y1
    while (x, y) != (x2 + dx, y2 + dy):
        diagonal_sum += grid[x][y]
        x += dx
        y += dy
    return diagonal_sum

for i in range(n):
    for j in range(n):
        for d1 in range(1, n):  
            for d2 in range(1, n): 
                i2, j2 = i + d1, j + d1 
                i3, j3 = i2 - d2, j2 + d2  
                i4, j4 = i3 - d1, j3 - d1 

                if 0 <= i2 < n and 0 <= j2 < n and \
                    0 <= i3 < n and 0 <= j3 < n and \
                    0 <= i4 < n and 0 <= j4 < n:
                    current_sum = (
                        get_diagonal_sum(i, j, i2, j2) +
                        get_diagonal_sum(i2, j2, i3, j3) +
                        get_diagonal_sum(i3, j3, i4, j4) +
                        get_diagonal_sum(i4, j4, i, j)
                    )

                    current_sum -= (
                        grid[i][j] + grid[i2][j2] +
                        grid[i3][j3] + grid[i4][j4]
                    )

                    max_sum = max(max_sum, current_sum)

print(max_sum)