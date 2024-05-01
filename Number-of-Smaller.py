n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
x = 0
cou = []
for i in range(m):
    while x < n and list1[x] <= list2[i]:
        x += 1
    cou.append(x)
print(cou)
