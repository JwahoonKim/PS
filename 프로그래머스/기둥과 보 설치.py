
# 기둥을 설치할 수 있는지 체크하는 함수
def canConstructCol(build_Info, result):
    x, y = build_Info[0], build_Info[1]
    # 1. y = 0이면 설치가능
    if y == 0:
        return True
    # 2. y != 0 이면 아래쪽에 기둥이 있거나 양 옆 중 한쪽이 보로 지지되어있으면 가능
    else:
        for structure in result:
            strX, strY = structure[0], structure[1]
            type = structure[2]
            # 아래쪽에 기둥이 있는 경우
            if type == 0:
                if strX == x and strY == y - 1:
                    return True
            # 양 옆 중 한쪽이 보로 지지 되어있는 경우
            elif type == 1:
                if strX == x - 1 and strY == y:
                    return True
                if strX == x and strY == y:
                    return True
    return False

# 보를 설치할 수 있는지 체크하는 함수
def canConstructBeam(build_Info, result):
    x, y = build_Info[0], build_Info[1]
    count = 0
    for structure in result:
        strX, strY = structure[0], structure[1]
        type = structure[2]
    # 1. 보의 양끝 중 한 곳에 기둥이 있는 경우
        if type == 0:
            if strX == x and strY == y - 1:
                return True
            elif strX == x + 1 and strY == y - 1:
                return True
    # 2. 보의 양 끝이 둘 다 보로 이어지는 경우
        elif type == 1:
            if strX == x - 1 and strY == y:
                count += 1
            elif strX == x + 1 and strY == y:
                count += 1
    if count == 2:
        return True
    return False


# 기둥을 삭제할 수 있는지 체크하는 함수
def canDeleteCol(build_Info, result):
    x, y = build_Info[0], build_Info[1]
    result.remove([x, y, 0])
    # 1. 기둥이 사라졌을 경우 원래 있던 기둥 한쪽 끝 당 세 개의 직선을 살펴봐(없으면 pass)
    # 즉, 총 6개의 직선이 설치조건에 만족하는지 check
    if [x, y - 1, 0] in result:
        if canConstructCol([x, y - 1, 0], result) == False:
            result.append([x, y, 0])
            return False
    if [x, y + 1, 0] in result:
        if canConstructCol([x, y + 1, 0], result) == False:
            result.append([x, y, 0])
            return False
    if [x - 1, y, 1] in result:
        if canConstructBeam([x - 1, y, 1], result) == False:
            result.append([x, y, 0])
            return False
    if [x, y, 1] in result:
        if canConstructBeam([x, y, 1], result) == False:
            result.append([x, y, 0])
            return False
    if [x - 1, y + 1, 1] in result:
        if canConstructBeam([x - 1, y + 1, 1], result) == False:
            result.append([x, y, 0])
            return False
    if [x, y + 1, 1] in result:
        if canConstructBeam([x, y + 1, 1], result) == False:
            result.append([x, y, 0])
            return False
    return True


# 보를 삭제할 수 있는지 체크하는 함수
def canDeleteBeam(build_Info, result):
    x, y = build_Info[0], build_Info[1]
    # 1. 보가 사라졌을 경우 원래 있던 보 한쪽 끝 당 세 개의 직선을 살펴봐(없으면 pass)
    # 2. 즉, 총 6개의 직선이 설치조건에 만족하는지 check
    x, y = build_Info[0], build_Info[1]
    result.remove([x, y, 1])
    if [x - 1, y, 1] in result:
        if canConstructBeam([x - 1, y, 1], result) == False:
            result.append([x, y, 1])
            return False
    if [x + 1, y, 1] in result:
        if canConstructBeam([x + 1, y, 1], result) == False:
            result.append([x, y, 1])
            return False
    if [x, y, 0] in result:
        if canConstructCol([x, y, 0], result) == False:
            result.append([x, y, 1])
            return False
    if [x, y - 1, 0] in result:
        if canConstructCol([x, y - 1, 0], result) == False:
            result.append([x, y, 1])
            return False
    if [x + 1, y, 0] in result:
        if canConstructCol([x + 1, y, 0], result) == False:
            result.append([x, y, 1])
            return False
    if [x + 1, y - 1, 0] in result:
        if canConstructCol([x + 1, y - 1, 0], result) == False:
            result.append([x, y, 1])
            return False
    return True
    

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y = build[0], build[1]
        structType, constType = build[2], build[3]
        # 1. 기둥건설
        if structType == 0 and constType == 1:
            if canConstructCol(build, answer) == True:
                answer.append([x, y, structType])
        # 2. 보 건설
        if structType == 1 and constType == 1:
            if canConstructBeam(build, answer) == True:
                answer.append([x, y, structType])
        # 3. 기둥 삭제
        if structType == 0 and constType == 0:
            canDeleteCol(build, answer)
        # 4. 보 파괴
        if structType == 1 and constType == 0:
            canDeleteBeam(build, answer)
    answer.sort()
    return answer
