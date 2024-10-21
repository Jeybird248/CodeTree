n = int(input())
arr1 = input().split()

m = int(input())
arr2 = input().split()

for num in arr2:
    if num in set(arr1):
        print(1, end = " ")
    else:
        print(0, end = " ")