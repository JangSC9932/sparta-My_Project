# # 완전탐색
# n = list(map(int, input().split()))
#
# cm = []
# for i in range(n[0]):
#     cm.append(int(input()))
#
#
#
# for i in range(max(cm), 1, -1):
#     a = 0
#     for j in cm:
#         a += j // i
#     if a >= n[1]:
#         print(i)
#         break

# 이분 탐색 적용

n = list(map(int, input().split()))

cm = []
for i in range(n[0]):
    cm.append(int(input()))

start = 1
end = max(cm)
while start <= end:
    a = 0
    mid = (start + end) // 2
    for j in cm:
        a += j // mid
    if a < n[1]:
        end = mid - 1
    else:
        start = mid + 1
    print(f"mid : {mid} start : {start} end : {end}")
