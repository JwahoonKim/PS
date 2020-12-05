T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    STR = input()
    for i in range(1, 11):
        length = i
        temp = ""
        for j in range(length):
            temp += STR[j]
        multiple = 30 // i
        if temp * multiple in STR:
            ans = length
            break
    print(f'#{test_case} {ans}')