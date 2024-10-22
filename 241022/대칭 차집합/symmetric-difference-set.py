n, m = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

not_A = set()

for num in A:
    if num not in B:
        not_A.add(num)

for num in B:
    if num not in A:
        not_A.add(num) 

print(len(not_A))