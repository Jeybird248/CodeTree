from sortedcontainers import SortedSet
n = int(input())
s = SortedSet()
for _ in range(n):
    command = input().split()
    if command[0] == "add":
        s.add(command[1])
    elif command[0] == "remove":
        s.remove(command[1])
    elif command[0] == "find":
        if command[1] in s:
            print("true")
        else:
            print("false")
    elif command[0] == "lower_bound":
        if s.bisect_left(command[1]) != len(s):
            print(s[s.bisect_left(command[1])])
        else:
            print(None)
    elif command[0] == "upper_bound":
        if s.bisect_right(command[1]) != len(s):
            print(s[s.bisect_right(command[1])])
        else:
            print(None)
    elif command[0] == "largest":
        if s:
            print(s[-1])
        else:
            print(None)
    elif command[0] == "smallest":
        if s:
            print(s[0])
        else:
            print(None)