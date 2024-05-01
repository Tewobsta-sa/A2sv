n = int(input())

for _ in range(n):
    size = int(input())
    lists = list(map(int, input().split()))
    temp = [lists[0]]
    for j in range(1, len(lists)):
        if temp[-1] * lists[j] < 0:
            temp.append(lists[j])
        elif temp[-1] < lists[j]:
            temp[-1] = lists[j]
    print(sum(temp))
