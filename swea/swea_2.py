test_case = int(input())

result = 0
for i in range(1,test_case+1):
    text = input()
    if text == text[::-1]:
        result = 1
    else:
        result = 0

    print(f'#{i} {result}')