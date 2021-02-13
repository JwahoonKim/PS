from collections import Counter

def solution(numbers, target):
    answer = 0
    #case는 numbers를 이용하여 만들 수 있는 모든 수
    case = dfs(0, [0], numbers)
    
    count = Counter(case)
    answer = count[target]
    return answer

# 1. i단계마다 만들 수 있는 경우의 수를 배열에 담고
# 2. i + 1 단계에 그 배열을 계속 넘겨주면
# 3. 마지막 단계에서 만들어진 배열은 numbers를 이용하여 만들수 있는 전체 경우를 담은 배열이다.
def dfs(i, nowArr, numbers):
    if i == len(numbers):
        return nowArr
    curNumber = numbers[i]
    nextArr = []
    for num in nowArr:
        nextArr.append(num + curNumber)
        nextArr.append(num - curNumber)
    return dfs(i + 1, nextArr, numbers)

numbers = [1,1,1,1,1]
target = 3
print(dfs(0,[0], numbers))

