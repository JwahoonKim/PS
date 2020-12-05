T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    count = [0] * 101
    score = list(map(int, input().split()))
    for i in score:
        count[i] += 1
    MAX = max(count)
    for i in range(100, -1, -1):
        if MAX == count[i]:
            ans = i
            break
    print(f'#{num} {ans}')