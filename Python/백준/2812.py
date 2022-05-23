n, k = map(int, input().split())
number = list(map(int, input()))
answer = []
K = k

for i in range(n):
    while K > 0 and answer and answer[-1] < number[i]:
        answer.pop()
        K -= 1
    answer.append(number[i])
print(''.join(map(str, answer[:n - k])))
