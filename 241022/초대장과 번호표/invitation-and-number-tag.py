N, G = map(int, input().split())
groups = [[] for _ in range(G)]
person_in_groups = [[] for _ in range(N+1)]
uninvited_count = [0] * G

for i in range(G):
    arr = list(map(int, input().split()))[1:]
    groups[i] = arr
    uninvited_count[i] = len(arr)
    for num in arr:
        person_in_groups[num].append(i)

q = [1]
visited_people = set([1])
answer = 0

while q:
    person = q.pop(0)
    answer += 1

    for group in person_in_groups[person]:
        uninvited_count[group] -= 1 
        
        if uninvited_count[group] == 1: 
            for member in groups[group]:
                if member not in visited_people:
                    visited_people.add(member)
                    q.append(member)

print(answer)