from collections import deque
t = int(input())

# deque 사용시
t_deque_list = deque(i for i in range(1, t+1))
print(t_deque_list)
while len(t_deque_list) > 1:
    print(f"카드 목록 : {list(t_deque_list)}")
    # 카드 삭제
    print(f"{t_deque_list.popleft()} 카드 삭제 --> {list(t_deque_list)}")
    # 첫번째 카드 뒤로 빼기
    t_deque_list.append(t_deque_list.popleft())
    print(f"첫번때 카드 뒤로 빼기 {list(t_deque_list)}")
print(t_deque_list[0])


# list 사용시
t_list = [i for i in range(1, t+1)]

while len(t_list) > 1:
    print(f"카드 목록 : {t_list}")
    # 카드 삭제
    print(f"{t_list.pop(0)} 카드 삭제 --> {t_list}")
    # 첫번째 카드 뒤로 빼기
    t_list.append(t_list.pop(0))
    print(f"첫번때 카드 뒤로 빼기 {t_list}")
print(t_list[0])


# 카드 목록 : [1, 2, 3, 4, 5, 6]
# 1 카드 삭제 --> [2, 3, 4, 5, 6]
# 첫번때 카드 뒤로 빼기 [3, 4, 5, 6, 2]
# 카드 목록 : [3, 4, 5, 6, 2]
# 3 카드 삭제 --> [4, 5, 6, 2]
# 첫번때 카드 뒤로 빼기 [5, 6, 2, 4]
# 카드 목록 : [5, 6, 2, 4]
# 5 카드 삭제 --> [6, 2, 4]
# 첫번때 카드 뒤로 빼기 [2, 4, 6]
# 카드 목록 : [2, 4, 6]
# 2 카드 삭제 --> [4, 6]
# 첫번때 카드 뒤로 빼기 [6, 4]
# 카드 목록 : [6, 4]
# 6 카드 삭제 --> [4]
# 첫번때 카드 뒤로 빼기 [4]
