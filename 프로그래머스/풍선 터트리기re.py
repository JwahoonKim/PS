def solution(a):
    answer = 1
    # a 의 최소값을 기준으로 왼쪽의 살아남는 풍선개수 세기 
    M = min(a)
    leftMin = a[0]
    i = 1
    while(leftMin != M):
        if leftMin >= a[i]:
            answer += 1
            leftMin = a[i]
        i += 1
    
    #오른쪽확인
    a.reverse()
    leftMin = a[0]
    i = 1
    while(leftMin != M):
        if leftMin >= a[i]:
            answer += 1
            leftMin = a[i]
        i += 1
    return answer

a = [9,-1,-5]
print(solution(a))