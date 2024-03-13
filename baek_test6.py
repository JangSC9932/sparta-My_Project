n = int(input())
a = set(list(map(int, input().split())))
n2 = int(input())
m = list(map(int, input().split()))

for i in m:
    if i in a:
        print(1)
    else:
        print(0)
