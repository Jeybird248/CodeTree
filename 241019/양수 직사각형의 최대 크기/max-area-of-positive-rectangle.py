n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_total_size = 0
negative_found = False
for x1 in range(n):
    for y1 in range(m):
        if grid[x1][y1] < 0:
            continue

        for x2 in range(x1, n):
            for y2 in range(y1, m):
                negative_found = False
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        if grid[i][j] < 0:
                            negative_found = True
                            break
                    if negative_found:
                        break
                
                if not negative_found:
                    size = (x2 - x1 + 1) * (y2 - y1 + 1)
                    max_total_size = max(max_total_size, size)
                    
print(max_total_size)