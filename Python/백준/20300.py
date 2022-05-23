# sort 한 후 양 끝에서 하나씩 뽑아서 근손실 체크
n = int(input())
answer = 0
muscle_loss = list(map(int, input().split()))

muscle_loss.sort()

# 운동기구가 홀수개면 제일 큰 근손실 운동기구 하나 뽑기
if len(muscle_loss) % 2 == 1:
    answer = muscle_loss.pop()

while(muscle_loss):
    answer = max(answer, muscle_loss.pop(0) + muscle_loss.pop())

print(answer)
