word = input()
d = {}

for char in word:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

found = False
for char in d:
    if d[char] == 1:
        print(char)
        found = True
        break
if not found:
    print("None")