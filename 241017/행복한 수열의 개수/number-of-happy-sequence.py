n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

happy_counter = 0
def check_happy(sequence, seq_type, index):
    global happy_counter

    current = sequence[0]
    count = 1
    if count >= m:
        happy_counter += 1
        return
    for i in range(1, len(sequence)):
        if sequence[i] == current:
            count += 1
            if count >= m:
                happy_counter += 1
                break
        else:
            current = sequence[i]
            count = 1

for row in range(n):
    check_happy(grid[row], "row", row)

for col in range(n):
    column_sequence = [grid[row][col] for row in range(n)]
    check_happy(column_sequence, "column", col)

print(happy_counter)  # Debug: final count