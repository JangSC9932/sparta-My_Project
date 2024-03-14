import sys

sys.stdin = open("baekjoon/input.txt", "r")

t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))


def find_subsequence(input_n):
    print(f"input_n : {input_n}")
    if input_n == 0:
        return 0

    for i in range(input_n):
        print(f"a[i] : {a[i]}")
        if k == a[i] + find_subsequence(input_n - 1):
            print("들옴")




