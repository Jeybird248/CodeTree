n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for num in arr1:
    if num in arr2:
        print(1, end = " ")
    else:
        print(0, end = " ")