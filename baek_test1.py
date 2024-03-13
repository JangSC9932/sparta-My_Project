from pprint import pprint

n = 4

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s1 = []
s2 = []
b = []
a = []
result = 0
for i in range(n):

    # a = list(map(int, input().split()))
    if i == 0:
        a.append([123, 1, 1])
    elif i == 1:
        a.append([356, 1, 0])
    elif i == 2:
        a.append([327, 2, 0])
    elif i == 3:
        a.append([489, 0, 1])


for j in a:
    for k in range(1, len(a)):
        print("JJ")
        print(j)
        print("KK")
        print(a[k])

pprint(a)