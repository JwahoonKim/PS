# 2차원 배열로 입력값 받기
num = int(input())
time = [[int(x) for x in input().split()] for y in range(num)]

#조건에 맞게 정렬
time.sort()
time.sort(key = lambda x:x[1])

#고를 수 있는 것 중 가장 빨리 끝나는 것을 고르면 됨
count = 1
i = 1
end_time = time[0][1]
# 고를 수 있는 것
while i < num:
    if end_time <= time[i][0]:
        end_time = time[i][1]
        count += 1 
        i += 1
    else: i += 1
#print(end_time)
#결과 출력
print(count)
