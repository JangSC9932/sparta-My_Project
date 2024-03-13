a = []
for i in range(9):
    a.append(list(map(int, input().split())))
b = []
for j, i in enumerate(a, 1):
    b.append([max(i), j, i.index(max(i))+1])
print(max(b)[0])
print(f"{max(b)[1]} {max(b)[2]}")
