import sys
sys.stdin = open("input.txt", "r")

t = int(input())

total = 0
for case in range(t):
    n = input()
    temp_list = []
    print(f"case {case+1} : {n}")
    for i in n:
        if temp_list and temp_list[-1] == i:
            print(f"{temp_list} 에서 마지막에 넣은 {i} 빼기")
            temp_list.pop()
        else:
            temp_list.append(i)
            print(f"{i} 추가 -> {temp_list}")
    print(f"결과 : {temp_list}")
    if len(temp_list) == 0:
        total += 1
print(total)


# case 1 : ABAB
# A 추가 -> ['A']
# B 추가 -> ['A', 'B']
# A 추가 -> ['A', 'B', 'A']
# B 추가 -> ['A', 'B', 'A', 'B']
# 결과 : ['A', 'B', 'A', 'B']
# case 2 : AABB
# A 추가 -> ['A']
# ['A'] 에서 마지막에 넣은 A 빼기
# B 추가 -> ['B']
# ['B'] 에서 마지막에 넣은 B 빼기
# 결과 : []
# case 3 : ABBA
# A 추가 -> ['A']
# B 추가 -> ['A', 'B']
# ['A', 'B'] 에서 마지막에 넣은 B 빼기
# ['A'] 에서 마지막에 넣은 A 빼기
# 결과 : []
# 2