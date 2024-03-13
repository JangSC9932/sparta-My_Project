import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    n_list = list(map(int, input().split()))

    # 최대값 기준으로 잘라서 비교하기
    max_number = max(n_list)
    max_number_index = n_list.index(max_number)

    a = 0
    for i in n_list[max_number_index:]:
        if n_list[q] <= i:
            a += 1

    b = 0
    for i in n_list[:max_number_index]:
        if n_list[q] < i:
            b += 1

    print(n_list)
    print(n_list[max_number_index:])
    print(n_list[:max_number_index])
    print(max_number)
    print(max_number_index)
    print(a + b)