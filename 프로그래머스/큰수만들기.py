# 왜 시간초과지
def solution(number, k):
    answer = ""
    answerLength = len(number) - k
    needLength = len(number) - k
    numList = list(number)
    i = "9"
    while 1:
        # 시간줄이기용(맨앞자리가 9면 그냥 바로 넣기)
        if numList[0] == 0:
            answer += numList[0]
            if len(answer) == answerLength:
                break
            numList = numList[1:]
            needLength -= 1
            i = "9"
        if i not in numList:
            i = str(int(i) - 1)
            continue
        cur = numList.index(i)
        # 선택해도 되는 경우(선택한 숫자 뒷쪽을 활용해 나머지 답을 만들 수 있는 경우)
        if len(numList[cur + 1 :]) >= needLength - 1:
            answer += numList[cur]
            if len(answer) == answerLength:
                break
            numList = numList[cur + 1 :]
            needLength -= 1
            i = "9"
        # 선택하면 안되는 경우
        else:
            i = str(int(i) - 1)
            continue
    return answer


if __name__ == "__main__":
    k = 2
    number = "1924"
    print(solution(number, k))