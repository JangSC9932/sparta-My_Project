# test. n의 배수
# https://school.programmers.co.kr/learn/courses/30/lessons/181937

num = 34
n = 3
answer_1 = 0

if num % n == 0:
    answer_1 = 1

print(answer_1)

# test. 문자열의 앞의 n글자
# https://school.programmers.co.kr/learn/courses/30/lessons/181907

my_string = "He110W0r1d"
n = 5

print(my_string[:n])

# test. 이어 붙인 수
# https://school.programmers.co.kr/learn/courses/30/lessons/181928

num_list = [3, 4, 5, 2, 1]
num1 = ""
num2 = ""

for num in num_list:
    if num % 2 == 0:
        num1 += str(num)
    else:
        num2 += str(num)

print(int(num1)+int(num2))