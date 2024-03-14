t = int(input())

for case in range(t):
    n = input()
    n_list = []
    try:
        for i in n:
            if i == "(":
                n_list.append(i)
            else:
                if n_list[-1] == "(":
                    n_list.pop()
        if len(n_list) == 0:
            print("YES")
        else:
            print("NO")
    except IndexError:
        print("NO")