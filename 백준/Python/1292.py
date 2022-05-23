seq = [0]
start, end = map(int, input().split())
for number in range(1, 1001):
    seq.extend([number] * number)
answer = sum(seq[start : end + 1])

print(answer)