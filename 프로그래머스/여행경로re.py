def solution(tickets):
    answer = []
    stack = ['ICN']
    # 출발지 : 도착지 정보를 hash화
    hash = dict()
    for ticket in tickets:
        start, end = ticket[0], ticket[1]
        if start in hash:
            hash[start].append(end)
        else:
            hash[start] = [end]
    
    # hash의 value들을 알파벳 내림차순으로 정렬
    for startPoint in hash:
        hash[startPoint].sort(reverse=True)
    while(stack):
        now = stack[-1]
        if now in hash and len(hash[now]) != 0:
            next = hash[now].pop()
            stack.append(next)
        else:
            answer.append(stack.pop())
    # answer를 거꾸로하면 정답이 나옴
    answer = [answer[i] for i in range(-1, -len(answer) - 1,-1)]
    return answer

tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(tickets))