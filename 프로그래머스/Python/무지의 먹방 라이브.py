def solution(food_times, k):
    # 방송 중단 전 음식 다먹으면 return -1
    total = sum(food_times)
    if total <= k:
        return -1

    length = len(food_times)
    foodTimesWithIndex = []

    for i in range(length):
        foodTimesWithIndex.append([food_times[i], i + 1])
    foodTimesWithIndex.sort(reverse=True)

    누적 = 0
    while 1:
        min = foodTimesWithIndex[-1][0] - 누적
        # k가 가장 작은 음식시간 * length보다 커서
        # 여러번 반복되는 경우
        if k >= min * length:
            k -= min * length
            length -= 1
            누적 += min
            foodTimesWithIndex.pop()
        # k가 한바퀴 도는 데 걸리는 시간보다 적은 경우
        elif k <= length:
            break
        # k가 한바퀴이상 도는데
        # 음식 하나를 다 먹지는 못하는 시간인 경우
        else:
            while 1:
                min -= 1
                if k >= min * length:
                    k -= min * length
                    break
    foodTimesWithIndex = sorted(foodTimesWithIndex, key=lambda x: x[1])
    return foodTimesWithIndex[k % length][1]


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))