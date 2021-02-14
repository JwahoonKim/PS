from collections import deque
from copy import deepcopy

#두 단어가 한글자만 다를 경우 변환가능 --> True 리턴하는 함수
def canChange(word1, word2):
    length = len(word1)
    count = 0
    for i in range(length):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    return False


def solution(begin, target, words):
    q = deque()
    q.append([begin])
    answer = None
    # target이 words안에 없는 경우
    if target not in words:
        return 0
    while(q):
        now = q.popleft()
        # 큐에는 단어 가능한 변화 진행상태가 들어가있음
        # ex.) (hit, hot, dot) , (hit, hot, iot) 

        # now에 target이 있다면 begin --> target으로 변화했다는 의미이므로 그게 최소변화 정답이고 while문 break 
        if target in now:
            answer = now
            break
        for word in words:
            if word not in now:
                if canChange(now[-1], word):
                    tmp = deepcopy(now)
                    tmp.append(word)
                    q.append(tmp)
    # answer가 나오지않았다면 answer는 처음 그대로 None일 것이고 그러면 정답 0
    if not answer:
        return 0

    # answer = (hit , hot, dot, dog, cog) 이므로 
    # len - 1이 정답
    return len(answer) - 1
