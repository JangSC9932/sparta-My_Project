def insertion_sort(array_list):
    for i in range(1, len(array_list)):
        key = array_list[i]
        print(f"key = {key}")
        for j in range(i):
            print(f"비교대상[인덱스] : {array_list[j]}[{j}]")
            if array_list[j] > key:
                print(f"key의 크기가 작으므로 {array_list[j]} 앞에 삽입")
                array_list.insert(j, array_list.pop(i))
                print(f"결과 : {array_list}")
                break
    return array_list


print(insertion_sort([4, 1, 6, 3, 5, 7, 2]))

# key = 1
# 비교대상[인덱스] : 4[0]
# key의 크기가 작으므로 4 앞에 삽입
# 결과 : [1, 4, 6, 3, 5, 7, 2]
# key = 6
# 비교대상[인덱스] : 1[0]
# 비교대상[인덱스] : 4[1]
# key = 3
# 비교대상[인덱스] : 1[0]
# 비교대상[인덱스] : 4[1]
# key의 크기가 작으므로 4 앞에 삽입
# 결과 : [1, 3, 4, 6, 5, 7, 2]
# key = 5
# 비교대상[인덱스] : 1[0]
# 비교대상[인덱스] : 3[1]
# 비교대상[인덱스] : 4[2]
# 비교대상[인덱스] : 6[3]
# key의 크기가 작으므로 6 앞에 삽입
# 결과 : [1, 3, 4, 5, 6, 7, 2]
# key = 7
# 비교대상[인덱스] : 1[0]
# 비교대상[인덱스] : 3[1]
# 비교대상[인덱스] : 4[2]
# 비교대상[인덱스] : 5[3]
# 비교대상[인덱스] : 6[4]
# key = 2
# 비교대상[인덱스] : 1[0]
# 비교대상[인덱스] : 3[1]
# key의 크기가 작으므로 3 앞에 삽입
# 결과 : [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]

