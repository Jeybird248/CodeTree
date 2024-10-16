n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# L-block transformations (4 rotations)
blocks = [
    [[1, 0], [1, 1]],  # Original
    [[0, 1], [1, 1]],  # Rotated 90°
    [[1, 1], [1, 0]],  # Rotated 180°
    [[1, 1], [0, 1]],  # Rotated 270°
    [[1, 1, 1]],  # Horizontal
    [[1], [1], [1]]  # Vertical
]

def sum_of_block(grid, block, start_i, start_j):
    total_sum = 0
    for i in range(len(block)):
        for j in range(len(block[0])):
            total_sum += grid[start_i + i][start_j + j] * block[i][j]
    return total_sum

max_sum = 0

for block in blocks:
    block_height = len(block)
    block_width = len(block[0])
    for i in range(n - block_height + 1):
        for j in range(m - block_width + 1):
            current_sum = sum_of_block(grid, block, i, j)
            max_sum = max(max_sum, current_sum)

print(max_sum)