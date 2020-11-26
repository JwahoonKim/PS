##에라토스테네스의 체 (런타임에러)



#N,K 값 정수 자료형으로 받기 (방법 다시 check)
#line 9 에서 range(2,N+1) 로 하면 empty sequence 에러가 뜸 왜그러지
N,K = map(int,input().split())

# 2 ~ N 까지 배열만들기 & 변수 설정
arr = list(range(1,N+1))  
Max = len(arr) + 1 
count = 0 
ref = 2
i = 1

#2 ~ N 의 배수까지 반복
for j in list(range(2,N+1)):
#2의 배수 지우기
    while i*ref <= max(arr):
        #수가 이미 지워졌을 때 넘어가기
        if i*ref not in arr:
            i += 1
            continue
        
        arr.remove(i*ref)
        count += 1
        if count == K :
            print(i*ref)
        i += 1
    ref += 1
    i = 1









# 백준 답안코드
# N, K = map(int, input().split())

# prime_number = [True for _ in range(N+1)]
# num = 1

# for i in range(2, N+1):
#     if prime_number[i] == True:
#         for j in range(i, N+1, i):
#             if prime_number[j] == False:
#                 continue
#             if num == K:
#                 print(j)
#             prime_number[j]= False
#             num += 1
