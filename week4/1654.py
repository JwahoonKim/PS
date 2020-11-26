#변수 받기
k,n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

#이진 탐색을 위한 변수 설정
start = 1 #생각없이 0 쓰지말자 start는 탐색할 가장 작은 값
end = max(arr)
flag = 0

#이진탐색
while(start <= end):
    count =0
    mid = (start + end) // 2
    
    for cable in arr:
        count += cable // mid  # 몫 = 케이블 잘린 개수
    
    if(count >= n): # 케이블 수가 많으면 더 길게 잘라보기
        flag = mid
        start = mid + 1
    elif(count < n): #케이블 수가 적으면 더 짧게 잘라보기
        end = mid - 1

print(flag)