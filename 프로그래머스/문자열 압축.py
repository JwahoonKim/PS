def solution(s):
    length = len(s)
    answer = length
    # 1 ~ length 까지로 잘라봐 그리고 비교해서 출력
    for i in range(1, length // 2 + 1):
        cutWord = []
        step = 0
        # i 길이만큼 잘라서 배열에 append
        while step + i <= length:
            cutWord.append(s[step : step + i])
            step += i
        # 마지막 남은 부분까지 append
        cutWord.append(s[step:])

        result = ""
        now = cutWord[0]
        repeat = 1
        # 문자열 압축하는 과정
        for i in range(1, len(cutWord)):
            # 같은 단어가 나오면 now에 모으기
            if cutWord[i] == now:
                repeat += 1
            # 다른 단어가 나오면 이전까지 모았던거 압축
            else:
                # 한번만 반복됐으면 앞에 숫자 생략 아니면 반복수 쓰기
                result += now if repeat == 1 else str(repeat) + now
                repeat = 1
                now = cutWord[i]
        # 마지막 남은부분까지 넣어주기 
        result += now if repeat == 1 else str(repeat) + now
        # 길이비교해서 더 짧은게 정답
        answer = min(answer, len(result))
    return answer


print(solution("abcabcdede"))
