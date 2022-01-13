def solution(numbers, hand):
    answer = ''
    leftHand, rightHand = [0, 3], [2, 3]
    keyPadMap = dict()
    keyPadMap[0] = [1, 3]
    
    for i in range(1, 10):
        keyPadMap[i] = [(i - 1) % 3, (i - 1) // 3]
    
    leftNumbers = [1,4,7]
    rightNumbers = [3,6,9]

    for number in numbers:
        if number in leftNumbers:
            answer += "L"
            leftHand = keyPadMap[number]
        elif number in rightNumbers:
            answer += "R"
            rightHand = keyPadMap[number]
        else:
            x, y = keyPadMap[number]
            leftDist = abs(leftHand[0] - x) + abs(leftHand[1] - y)
            rightDist = abs(rightHand[0] - x) + abs(rightHand[1] - y)
            # 가까운거 체크
            if leftDist > rightDist or (leftDist == rightDist and hand == "right"):
                answer += "R"
                rightHand = [x, y]
            elif rightDist > leftDist or (leftDist == rightDist and hand == "left"):
                answer += "L"
                leftHand = [x, y]
    return answer

numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
print(solution(numbers, hand))