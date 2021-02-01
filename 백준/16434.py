import sys

input = sys.stdin.readline

n, Hattack = map(int, input().split())
needHp = 0
answer = 0

for i in range(n):
    type, attack, hp = map(int, input().split())
    if type == 1:
        turn = hp // Hattack
        if hp % Hattack == 0:
            needHp += attack * (turn - 1)
            # 필요한 체력량은 최종단계에서만 안죽는경우가 아니고중간단계에서도 안죽어야함
            answer = max(needHp, answer)
        else:
            needHp += attack * turn
            answer = max(needHp, answer)
    else:
        Hattack += attack
        if needHp - hp >= 0:
            needHp -= hp
        else:
            needHp = 0
# 정답출력
print(answer + 1)
