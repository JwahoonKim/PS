T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = input()
    length = len(word)
    palin = ''
    for i in range(-1, -(length) - 1, -1):
        palin += word[i]
    if palin == word:
        ans = 1
    else: ans = 0
    print(palin)
    print(f'#{test_case} {ans}')
