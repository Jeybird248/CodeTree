n = int(input())
arr1 = set(map(str, input().split()))
m = int(input())
arr2 = set(map(str, input().split()))

for i in arr2:
    if i in arr1:
        print(1)
    else:
        print(0)