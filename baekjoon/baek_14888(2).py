import sys,itertools
sys.stdin = open("input.txt", "r")

n = int(input())
num_list = list(map(int, input().split(' ')))
oper_list = list(map(int, input().split(' ')))
answer_list = []

print(num_l)
def calculate(index=0, answer=num_list[0]):
    original = answer
    print(f"original : {original}")
    print(f"oper_list : {oper_list}")
    print(f"index : {index}")
    if index == len(num_list)-1:
        answer_list.append(answer)
        return
    for i in range(4):
        print(oper_list[i])
        if oper_list[i] > 0:
            if i == 0:
                answer += num_list[index + 1]
            elif i == 1:
                answer -= num_list[index + 1]
            elif i == 2:
                answer *= num_list[index + 1]
            else:
                if answer * num_list[index + 1] < 0:
                    answer = (answer*-1 // num_list[index + 1])*-1
                else :
                    answer = answer // num_list[index + 1]
            oper_list[i] -= 1
            calculate(index+1, answer)
            oper_list[i] += 1
            answer = original


calculate()
print(max(answer_list))
print(min(answer_list))