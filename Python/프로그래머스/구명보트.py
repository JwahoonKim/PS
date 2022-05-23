from collections import deque

# 1. 가장 무거운 사람 우선 뽑고
# 2. 가장 작은 사람을 뽑아서
# 3. 둘 다 탈출 가능한지 체크
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque()
    for person in people:
        q.append(person)
    while(q):
        heaviest = q.pop()
        if q:
            lightest = q[0]
            if heaviest + lightest <= limit:
                q.popleft()
                answer += 1
            else:
                answer += 1
        else:
            answer += 1
    return answer


people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))