def checkScovile(arr, K):
    for i in arr:
        if i < K:
            return False
    return True

def solution(scoville, K):
    count = 0
    
    return 