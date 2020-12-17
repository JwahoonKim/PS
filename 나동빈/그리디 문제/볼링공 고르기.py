# N, M = map(int, input().split())
# data = list(map(int, input().split()))
# count = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         if data[i] != data[j]:
#             count += 1
# print(count)


# 시간복잡도를 줄인 풀이
N, M = map(int, input().split())
data = list(map(int, input().split()))
arr = [0] * 11
ans = 0
for x in data:
    arr[x] += 1
for i in range(1, M + 1):
    N -= arr[i]
    ans += arr[i] * N
print(ans)