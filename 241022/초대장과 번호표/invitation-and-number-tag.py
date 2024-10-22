N, G = map(int, input().split())
groups = [[] for _ in range(N+1)]

for i in range(G):
    arr = list(map(int, input().split()))[1:]
    for num in arr:
        groups[num].append(i)

q = [1]
visited_groups = set()
visited_elements = set([1])
answer = 0

while q:
    temp = q.pop(0)
    answer += 1

    for group in groups[temp]:
        if group in visited_groups:
            continue
        visited_groups.add(group)

        for num in groups[temp]:
            if num not in visited_elements:
                visited_elements.add(num)
                q.append(num)

print(answer)