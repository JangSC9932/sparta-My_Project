# test. 특정 문자 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120826
import math

my_string = "abcdef"
letter = "f"

print(my_string.replace(letter,''))

# test. 아이스 아메리카노
# https://school.programmers.co.kr/learn/courses/30/lessons/120819

answer = []
price = 5500
money = 1000

answer.append(int(money / price))
answer.append(int(money - (price * answer[0])))

print(answer)

# test. 피자 나눠벅기(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120814

piece = 7
n = 1

print(math.ceil(n / piece))

# test. 최댓값 만들기(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120847

numbers = [0, 31, 24, 10, 1, 9]
numbers.sort(reverse=True)
print(numbers[0]*numbers[1])

# test. 배열 두배 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120809

numbers = [1, 2, 3, 4, 5]

for i, number in enumerate(numbers):
    numbers[i] *= 2

print(numbers)

# test. 피자 나눠 먹기(3)
# https://school.programmers.co.kr/learn/courses/30/lessons/120816

piece = 4
n = 12

print(math.ceil(n/piece))

# test. 짝수 홀수 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120824

numbers = [1, 3, 5, 7]
answer = [0, 0]

for number in numbers:
    if number % 2 == 0:
        answer[0] += 1
    else:
        answer[1] += 1
print(answer)

# test. 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120906

n = 1234
answer = 0

for i in str(n):
    answer += int(i)

print(answer)

# test. 배열의 유사도
# https://school.programmers.co.kr/learn/courses/30/lessons/120903

s1 = ["n", "omg"]
s2 = ["m", "dot"]
answer = 0
for s in s1:
    if s in s2:
        answer += 1

print(answer)

# test. 양꼬치
# https://school.programmers.co.kr/learn/courses/30/lessons/120830

a = 12000
b = 2000
n = 64
k = 6

print((a*n)+(b*(k-(n//10))))

# test. 세균증식
# https://school.programmers.co.kr/learn/courses/30/lessons/120910

n = 7
t = 15

print(n*(2**t))

# test. 삼각형의 완성조건
# https://school.programmers.co.kr/learn/courses/30/lessons/120889

sides = [199, 72, 222]
sides.sort()
answer = 2
if sides[2] < (sides[0]+sides[1]):
    answer = 1

print(answer)

# test. 중앙값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120811

array = [1, 2, 7, 10, 11]
array.sort()
index = len(array)//2

print(array[len(array) // 2])
print(index)
print(array[index])

# test. 짝수는 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120813

n = 10
answer = []
for i in range(n):
    if (n-(n-i)) % 2 != 0:
        answer.append(i)

print(answer)

# test. 순서쌍의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120836

n = 100
answer = 0
for i in range(1,n+1):
    if n % i == 0:
        answer += 1
print(answer)

# test. 모음제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120849

my_string = "nice to meet you"
sub_string = ["a", "e", "i", "o", "u"]

for string in sub_string:
    if string in my_string:
        my_string = my_string.replace(string,"")

print(my_string)

# test. 문자 반복 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120825

my_string = "hello"
n = 3
answer = ""

for string in my_string:
    for i in range(n):
        answer += string

print(answer)

print("".join(i * n for i in my_string))


# test. 옷가게 할인 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/120818

price = 10
if price >= 500000:
    price = price - int(price * 0.2)
elif price >= 300000:
    price = price - int(price * 0.1)
elif price >= 100000:
    price = price - int(price * 0.05)

print(int(price))

# test. 제곱수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120909

if isinstance(144 ** 0.5, int):
    answer = 1
else:
    answer = 2
print((144 ** 0.5).is_integer())

# test. 숨어있는 숫자의 덧셈(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120851

my_string = "1a2b3c4d123"
answer = 0
for string in my_string:
    if string.isdigit():
        answer += int(string)

print(answer)




