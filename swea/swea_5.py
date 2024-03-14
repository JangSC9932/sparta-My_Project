import sys
sys.stdin = open("baekjoon/input.txt", "r")

t = int(input())

for case in range(1, t+1):
    puzzle_size, block = map(int, input().split())
    puzzle = []
    for line in range(puzzle_size):
        puzzle.append("".join(list(map(str, input().split()))))

    total = 0
    for i in puzzle:
        total += i.split("0").count("1"*block)

    for i in range(puzzle_size):
        p_string = ""
        for j in puzzle:
            p_string += j[i]
        total += p_string.split("0").count("1"*block)

    print(f'#{case} {total}')