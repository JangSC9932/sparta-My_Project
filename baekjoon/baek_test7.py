from pprint import pprint

n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))
row = []
count = 0
for i in range(max(a, key=lambda x: x[1])[1] + 10):
    col = []
    for j in range(max(a, key=lambda x: x[0])[0] + 10):
        col.append(0)
    row.append(col)

for i in a:
    for i2 in range(i[0], i[0] + 10):
        for i3 in range(i[1], i[1] + 10):
            row[i3][i2] += 1

for i in row:
    for j in i:
        if j > 0:
            count += 1
pprint(row)
print(count)