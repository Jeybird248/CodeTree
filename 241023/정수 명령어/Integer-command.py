from sortedcontainers import SortedSet

s = SortedSet()
T = int(input())

for _ in range(T):
    k = int(input())
    for _ in range(k):
        command = input().split()
        if command[0] == "I":
            s.add(int(command[1]))
        elif command[0] == "D":
            if len(s):
                if command[1] == "1":
                    s.remove(s[-1])
                else:
                    s.remove(s[0])
    if len(s):
        print(s[-1], s[0])
    else:
        print("EMPTY")