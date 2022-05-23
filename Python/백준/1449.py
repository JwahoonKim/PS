#수도공 항승
#변수 정보 받기
N,L = map(int, input().split())
fix = list(map(int, input().split()))

#필요한 수도관 길이 생성 + 거기에 False 값 넣기
#길이 생성할때 range의 두번째 항은 line 19에서 i = max(fix) 근처일 때 오류가 나지 않도록 조정해준것
arr = [False for i in range(1,max(fix)+L+1)]

#고장난 위치만 True로 바꿔주기
for i in fix:
    arr[i-1] = True

# 1항부터 True 찾아서 자기포함 L개 False 로 바꾸기 + count 하나 올려주기
count = 0
for i in list(range(0,max(fix))):
    if arr[i] == False:
        continue
    if arr[i] == True:
        for j in list(range(i,L+i)):
            arr[j] = False
    count += 1        

#결과 출력
print(count)

