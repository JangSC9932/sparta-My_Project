def bubble_sort(array_list):
    for i in range(len(array_list)-1):
        print(f"{i + 1}회전 시작 : {array_list}")
        for j in range(len(array_list) -1):
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