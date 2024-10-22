# Variable declaration and input:
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

# Insert all elements of sequence a into a HashSet.
set1 = set(arr1)

# Check if each element of sequence b is in sequence a.
for elem2 in arr2:
    # If not found, output 0.
    if elem2 not in set1:
        print(0)
    # If found, output 1.
    else:
        print(1)