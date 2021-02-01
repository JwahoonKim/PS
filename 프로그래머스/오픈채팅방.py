def solution(record):
    nameDict = {}
    result = []
    # enter로 들어온 애들, 닉네임 change한 애들을 dict에 넣어주기 위한 반복문
    for info in record:
        # log = [행동, 아이디, 닉네임]
        log = info.split()
        if log[0] == "Enter":
            nameDict[log[1]] = log[2]
        elif log[0] == "Change":
            nameDict[log[1]] = log[2]
    # 위 과정으로 닉네임이 다 바뀐 상태에서 채팅방에 표시하기
    for info in record:
        log = info.split()
        if log[0] == "Enter":
            result.append(f"{nameDict[log[1]]}님이 들어왔습니다.")
        elif log[0] == "Leave":
            result.append(f"{nameDict[log[1]]}님이 나갔습니다.")

    return result
