# 인접한 걸 못고르는 유형의 dp
def findMax(arr):
    # dp[n] = max( dp[n - 1] , dp[n - 2] + arr_n-2]
    length = len(arr)
    dp = [0] * length
    if length == 1:
        return arr[0]
    elif length == 2:
        return max(arr[0], arr[1])
    else:
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, length):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
    return dp[length - 1]


def solution(money):
    answer = 0
    # 0. money길이가 1,2,3인 경우 그냥 한 집 털어야함
    if len(money) <= 3:
        return max(money)
    # 1. 첫번째 집을 고르는 경우
    way1 = money[0] + findMax(money[2:-1])
    # 2. 마지막 집을 고르는 경우
    way2 = money[-1] + findMax(money[1:-2])
    # 3. 둘 다 안고르는 경우
    way3 = findMax(money[1:-1])
    answer = max(way1, way2, way3)
    return answer