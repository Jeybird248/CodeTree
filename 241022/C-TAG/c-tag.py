N, M = map(int, input().split())
A_group = [input().strip() for _ in range(N)]
B_group = [input().strip() for _ in range(N)]

def can_differentiate(A_group, B_group, i, j, k):
    seen = {}
    
    for paper in A_group:
        triplet = (paper[i], paper[j], paper[k])
        seen[triplet] = 'A'
    
    for paper in B_group:
        triplet = (paper[i], paper[j], paper[k])
        if triplet in seen:
            return False
    
    return True

valid_combinations = 0
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            if can_differentiate(A_group, B_group, i, j, k):
                valid_combinations += 1

print(valid_combinations)