n = int(input())
arr = []

for i in range(n):
    info = list(input().split())
    # 가입 순서 표기 : info = (나이, 이름, 가입순서) 
    info.append(int(i))
    arr.append(info)
    
#나이는 int 형으로 고쳐줌    
for i in range(n):
    arr[i][0] = int(arr[i][0])

#1.나이순 , 2.가입순으로 정렬
arr = sorted(arr, key = lambda x : (x[0], x[2]))

for i in range(n):
    print(arr[i][0], arr[i][1])