n = int(input())

s = set()
for _ in range(n):
    command = input().split()
    if command[0] == "find":
        if command[1] in s:
            print("true")
        else:
            print("false")
    elif command[0] == "add":
        s.add(command[1])
    else:
        s.remove(command[1])