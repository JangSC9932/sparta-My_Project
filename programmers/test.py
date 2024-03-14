# test. 배열의 평균값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120817
numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

answer = sum(numbers) / len(numbers)

print(answer)

# test. 머쓱이보다 키 큰 사람
# https://school.programmers.co.kr/learn/courses/30/lessons/120585

array = [180, 120, 140]
height = 190
answer = []

for i in array:
    if i > height:
        answer.append(i)

print(len(answer))

# test. 배열 원소의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120854

strlist = ["I", "Love", "Programmers."]
answer = []

for i in strlist:
    answer.append(len(i))
print(answer)

# test. 배열 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/120821

num_list = [1, 0, 1, 1, 1, 3, 5]
answer = []
num_list.reverse()

print(num_list)

# test. 중복된 숫자 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120583

answer = 0
array = [1, 1, 2, 3, 4, 5]
n = 1

for i in array:
    if n == i:
        answer += 1

print(answer)

# test. 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/120833

numbers = [1, 3, 5]
num1 = 1
num2 = 2
answer = []

answer = numbers[num1:(num2+1)]
print(answer)

# test. 문자열 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/120822

my_string = 'jaron'
answer = ''

answer = my_string[::-1]

print(answer)

# test. 편지
# https://school.programmers.co.kr/learn/courses/30/lessons/120898

message = "I love you~"
print(len(message)*2)

# test. 점의 위치 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120841

dot = [-7, 9]
answer = 0

if dot[0] > 0 and dot[1] > 0:
    answer = 1
elif dot[0] < 0 < dot[1]:
    answer = 2
elif dot[0] > 0 > dot[1]:
    answer = 4
else:
    answer = 3

print(answer)

# test. 문자열안에 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/120908

str1 = "ppprrrogrammers"
str2 = "pppp"
answer = 2

if str2 in str1:
    answer = 1

print(answer)

