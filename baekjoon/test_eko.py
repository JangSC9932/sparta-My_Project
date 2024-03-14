# 완전 탐색
# n, m = map(int, input().split())
# tree = list(map(int, input().split()))

# for i in range(1, max(tree)):
#     tree_clone = tree.copy()
#     for j in range(len(tree)):
#         tree_clone[j] -= i
#         if tree_clone[j] < 0:
#             tree_clone[j] = 0
#     if sum(tree_clone) == m:
#         print(i)
#         break

# 이분 탐색
# n, m = 4, 7
# tree = [20, 15, 10, 17]

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)
result = 0
while start <= end:
    cm = 0
    mid = (start + end) // 2
    for i in tree:
        if i > mid:
            cm += i - mid
    if cm >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)


