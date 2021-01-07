n = int(input())
house = list(map(int, input().split()))
dp = [0] * (n + 2)


def attack(i):
    if dp[i] > 0:
        return dp[i]
    if i >= len(house):
        return 0
    # i번째 house를 선택하는 경우
    way1 = house[i] + attack(i + 2)
    # i번째 house를 선택하지 않는 경우
    way2 = attack(i + 1)
    dp[i] = max(way1, way2)
    return max(way1, way2)


print(attack(0))