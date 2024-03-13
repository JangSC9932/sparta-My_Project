
n = int(input())
a = []
for i in range(n):
    b = []
    for num in str(i):
        b.append(num)
    if i+sum(map(int, b)) == n:
        a.append(i)
if a:
    print(min(a))
else:
    print(0)
