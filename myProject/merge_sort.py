def merge_sort(array_list):

    if len(array_list) <= 1:
        return array_list

    mid = len(array_list) // 2
    print(array_list)
    print("자르기")
    left = merge_sort(array_list[:mid])
    right = merge_sort(array_list[mid:])

    return merge(left, right)


def merge(left, right):
    print("비교하며 합치기")
    merged_list = []
    print(f"left : {left} | right : {right}")
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged_list.append(left.pop(left.index(left[0])))
        else:
            merged_list.append(right.pop(right.index(right[0])))
    print(f"합친 결과 : {merged_list + right}")
    return merged_list + right


print(merge_sort([4, 1, 4, 6, 3, 5, 9]))


# [4, 1, 6, 3, 5, 9]
# 자르기
# [4, 1, 6]
# 자르기
# [1, 6]
# 자르기
# 비교하며 합치기
# left : [1] | right : [6]
# 합친 결과 : [1, 6]
# 비교하며 합치기
# left : [4] | right : [1, 6]
# 합친 결과 : [1, 4, 6]
# [3, 5, 9]
# 자르기
# [5, 9]
# 자르기
# 비교하며 합치기
# left : [5] | right : [9]
# 합친 결과 : [5, 9]
# 비교하며 합치기
# left : [3] | right : [5, 9]
# 합친 결과 : [3, 5, 9]
# 비교하며 합치기
# left : [1, 4, 6] | right : [3, 5, 9]
# 합친 결과 : [1, 3, 4, 5, 6, 9]
# [1, 3, 4, 5, 6, 9]