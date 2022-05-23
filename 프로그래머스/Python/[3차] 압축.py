import sys
sys.setrecursionlimit(int(1e9))

# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
index = {chr(ord('A') + i) : i + 1 for i in range(26)}

def findLongestWord(w):
    if w in index:
        return w
    return findLongestWord(w[:-1])

def solution(msg):
    answer = []
    while msg:
        w = findLongestWord(msg) # 현재 입력과 일치하는 가장 긴문자열 w를 찾는다.
        answer.append(index[w]) # w에 해당하는 사전의 색인 번호를 출력하고,
        msg = msg[len(w):] # 입력에서 w를 제거한다.
        if msg: # 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
            index[w + msg[0]] = len(index) + 1
    return answer

print(solution('KAKAO'))