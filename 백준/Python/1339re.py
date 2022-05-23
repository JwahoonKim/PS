import sys

input = sys.stdin.readline

n = int(input())

number = [9,8,7,6,5,4,3,2,1,0]
# 알파벳이 무엇이 있고, 알파벳이 어느자리에 나왔는지에 대한 정보를 담는 dict
alpInfo = {}
words = []
answer = 0

for i in range(n):
    word = input().rstrip()
    words.append(word)
    length = len(word)
    # 알파벳이 어느자리에 나왔는지에 대한 정보를 담는 과정
    for i in range(len(word)):
        if word[i] in alpInfo.keys():
            alpInfo[word[i]] += 10 ** (length - i - 1) 
        else:
            alpInfo[word[i]] = 10 ** (length - i - 1)
# alpInfo 원소 예시 : (A, 10001) --> A는 만의자리, 일의자리 한번씩 등장했음
# alpInfo[1] 을 기준으로 내림차순 정렬한 뒤 첫번째 원소부터 9,8,7,6,... 을 곱하여 더하면 정답
alpInfo = sorted(alpInfo.items(), key = lambda x : x[1], reverse=True)
for i in range(len(alpInfo)):
    answer += alpInfo[i][1] * number[i]

print(answer)
