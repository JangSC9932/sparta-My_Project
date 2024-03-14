def selection_sort(array_list):
    temp_list = []
    for i in range(len(array_list)):
        for j in range(len(array_list)):
            if array_list[0] > array_list[j]:
                array_list[0], array_list[j] = array_list[j], array_list[0]
        print(f"최소값 : {array_list[0]}")
        temp_list.append(array_list.pop(0))
        print(f"{i+1} 회전 {temp_list} {array_list}")
    return temp_list


print(selection_sort([4, 1, 6, 3, 5]))

# 최솟값 : 1
# 1 회전 [1] [4, 6, 3, 5]
# 최솟값 : 3
# 2 회전 [1, 3] [4, 6, 5]
# 최솟값 : 4
# 3 회전 [1, 3, 4] [6, 5]
# 최솟값 : 5
# 4 회전 [1, 3, 4, 5] [6]
# 최솟값 : 6
# 5 회전 [1, 3, 4, 5, 6] []
# [1, 3, 4, 5, 6]


# 재귀함구 구현
def selection_sort_recursive(array_list):
    temp_list = []
    if len(array_list) == 1:
        print(f"{array_list} 추가")
        return array_list
    else:
        for i in range(len(array_list)):
            if array_list[0] > array_list[i]:
                array_list[0], array_list[i] = array_list[i], array_list[0]
        print(f"{array_list} 에서")
        temp_list.append(array_list.pop(0))
        print(f"{temp_list} 추가")
        return temp_list + selection_sort_recursive(array_list)


print(selection_sort_recursive([4, 1, 6, 3, 5]))



