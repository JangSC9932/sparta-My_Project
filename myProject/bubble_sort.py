def bubble_sort(array_list):
    for i in range(len(array_list) - 1):
        print(f"{i + 1}회전 시작 : {array_list}")
        for j in range(len(array_list) - 1 - i):
            print(f"{array_list} | {array_list[j]} 와 {array_list[j+1]} 비교")
            if array_list[j] > array_list[j+1]:
                a = array_list[j]
                b = array_list[j+1]
                array_list[j+1] = a
                array_list[j] = b
                print(f"교환 {array_list}")
        print(f"{i+1}회전 종료 : {array_list}")
    return array_list


print(bubble_sort([4, 1, 6, 3, 5]))

# 1회전 시작 : [4, 1, 6, 3, 5]
# [4, 1, 6, 3, 5] | 4 와 1 비교
# 교환 [1, 4, 6, 3, 5]
# [1, 4, 6, 3, 5] | 4 와 6 비교
# [1, 4, 6, 3, 5] | 6 와 3 비교
# 교환 [1, 4, 3, 6, 5]
# [1, 4, 3, 6, 5] | 6 와 5 비교
# 교환 [1, 4, 3, 5, 6]
# 1회전 종료 : [1, 4, 3, 5, 6]
# 2회전 시작 : [1, 4, 3, 5, 6]
# [1, 4, 3, 5, 6] | 1 와 4 비교
# [1, 4, 3, 5, 6] | 4 와 3 비교
# 교환 [1, 3, 4, 5, 6]
# [1, 3, 4, 5, 6] | 4 와 5 비교
# 2회전 종료 : [1, 3, 4, 5, 6]
# 3회전 시작 : [1, 3, 4, 5, 6]
# [1, 3, 4, 5, 6] | 1 와 3 비교
# [1, 3, 4, 5, 6] | 3 와 4 비교
# 3회전 종료 : [1, 3, 4, 5, 6]
# 4회전 시작 : [1, 3, 4, 5, 6]
# [1, 3, 4, 5, 6] | 1 와 3 비교
# 4회전 종료 : [1, 3, 4, 5, 6]
# [1, 3, 4, 5, 6]