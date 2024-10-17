n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def sum_of_block(grid, k, start_i, start_j):
    total_sum = 0
    for i in range(-k, k + 1):
        for j in range(-k, k + 1):
            if abs(i) + abs(j) <= k and 0 <= start_i + i < n and 0 <= start_j + j < n:
                total_sum += grid[start_i + i][start_j + j] * m
    return total_sum

max_sum = 0

for k in range(0, n):
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            current_sum = sum_of_block(grid, k, i, j)
            # print("found", current_sum, k, i, j, (k * k + (k + 1) * (k + 1)))

            if current_sum - (k * k + (k + 1) * (k + 1)) >= 0:
                max_sum = max(max_sum, current_sum // m)

print(max_sum)