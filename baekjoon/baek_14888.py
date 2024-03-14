import sys
import itertools

sys.stdin = open("input.txt", "r")

t = int(input())

n = list(map(int, input().split()))

m = list(map(int, input().split()))

m_list = []

print(f" 숫자 : {n}")
print(f" 연산자 : +({m[0]}) | -({m[1]}) | *({m[2]}) | /({m[3]})")
for index, i in enumerate(m):
    if index == 0:
        for j in range(i):
            m_list.append("+")
    if index == 1:
        for j in range(i):
            m_list.append("-")
    if index == 2:
        for j in range(i):
            m_list.append("*")
    if index == 3:
        for j in range(i):
            m_list.append("/")

# 연산자 경우의 수 구하기
temp_list = list(map(''.join, itertools.permutations(m_list)))
print(f" 연산자 경우의 수: {temp_list}")
reuslt_list = []
for i in temp_list:
    result = 0
    cal_text = ""
    for index, j in enumerate(n):
        if index > 0:
            # 나누기셈은 따로 조건 추가
            if i[index-1] == '/':
                result = abs(result) // n[index]
                cal_text += str(i[index-1]) + str(n[index])
            else:
                result = eval(str(result) + str(i[index-1]) + str(n[index]))
                cal_text += str(i[index-1]) + str(n[index])
        else:
            result += n[index]
            cal_text = str(n[index])
    print(cal_text)
    reuslt_list.append(result)
print(max(reuslt_list))
print(min(reuslt_list))


#  숫자 : [3, 4, 5]
#  연산자 : +(1) | -(0) | *(1) | /(0)
#  연산자 경우의 수: ['+*', '*+']
# 3+4*5
# 3*4+5
# 35
# 17