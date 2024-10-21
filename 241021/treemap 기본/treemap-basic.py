from sortedcontainers import SortedDict

n = int(input())
d = SortedDict()
for _ in range(n):
    row = input().split()
    if row[0] == "add":
        d[int(row[1])] = int(row[2])
    elif row[0] == "find":
        if int(row[1]) in d:
            print(d[int(row[1])])
        else:
            print("None")
    elif row[0] == "remove":
        d.pop(int(row[1]))
    else:
        if not d.values():
            print("None")
        else:
            for entry in d.keys():
                print(d[entry], end = " ")
            print()