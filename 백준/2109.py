import sys

input = sys.stdin.readline

n = int(input())
lectures = []
Maxday = 0
answer = 0
for i in range(n):
    pay, day = map(int, input().split())
    lectures.append([pay, day])
    # 가장 오래 기다려주는 날짜
    Maxday = max(day, Maxday)

lectures = sorted(lectures, key = lambda x : x[0], reverse=True)
schedule = [False for _ in range(Maxday)]

for i in range(n):
    pay, day = lectures[i]
    cur = day - 1
    if schedule[cur] == False:
        schedule[cur] = True
        answer += pay
    else:
        cur -= 1
        #해당 강연을 넣을 수 있는지 이전 날들도 쭉 체크
        while(cur >= 0):
            if schedule[cur] == False:
                schedule[cur] = True
                answer += pay
                break
            else:
                cur -= 1
print(answer)
        

