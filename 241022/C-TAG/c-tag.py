N, M = map(int, input().split())
A_group = [input().strip() for _ in range(N)]
B_group = [input().strip() for _ in range(N)]

def can_differentiate(A_group, B_group, positions):
    A_tuples = set()
    B_tuples = set()
    
    for paper in A_group:
        A_tuples.add((paper[positions[0]], paper[positions[1]], paper[positions[2]]))
    
    for paper in B_group:
        B_tuples.add((paper[positions[0]], paper[positions[1]], paper[positions[2]]))
    
    return A_tuples.isdisjoint(B_tuples)

valid_combinations = 0
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            if can_differentiate(A_group, B_group, [i, j, k]):
                valid_combinations += 1

print(valid_combinations)