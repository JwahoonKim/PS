

def solution(numbers, target):
    answer = 0
    case = dfs(0, [0], numbers)

    return answer

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

