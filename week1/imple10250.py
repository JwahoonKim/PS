#ACM 호텔
T = input()

for i in range(int(T)):
    #입력값 받기
    H,W,N = map(int,input().split())

    #빌딩을 배열로 표현 H:층 W:폭
    arr = [[i for i in range(W)]for j in range(H)]

    #층수 = 나머지 , 호수 = 몫
    if N%H == 0:
        floor = H
        Room = N // H
    else:    
        floor = N % H
        Room = N // H + 1

    print('%d%02d' %(floor,Room))
    