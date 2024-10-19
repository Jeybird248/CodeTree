n = int(input())
d = {}
for i in range(n):
    j = input().split()
    if len(j) == 2:
        operator, num1 = j
    else:
        operator, num1, num2 = j
    if operator == "add":
        d[num1] = num2
    elif operator == "remove":
        del d[num1]
    else:
        if num1 in d:
            print(d[num1])
        else:
            print("None")