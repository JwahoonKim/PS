T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    profit = 0
    N = int(input())
    price = list(map(int,input().split()))
    MAX = price[-1]
    for i in range(len(price) - 2, -1, -1):
        if MAX < price[i]:
            MAX = price[i]
        else: profit += MAX - price[i]
    print(f'#{test_case} {profit}')
    
