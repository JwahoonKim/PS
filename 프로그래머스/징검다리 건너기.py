from itertools import filterfalse


INF = int(1e9)

def serialZero(arr, k):
    zeroIndex = arr.find(0)
    if zeroIndex == -1:
        return False
    else:
        


def solution(stones, k):
    while(1):
        
        mini = min(filter(lambda x : x > 0, stones))
        answer += mini
        stones [i - mini if i > 0 else 0 for i in stones]
        flag = False
        for i in range(len(stones)):
            if stones[i] == 0:
                count += 1
            if count == k:
                flag = True
                break
            if stones[i] != 0:
                count = 0
        if flag == True:
            break
        else:
            answer += 1
            stones = [i - 1 if i > 0 else i for i in stones]
    return answer


if __name__ == '__main__':
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))