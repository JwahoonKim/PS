#같은 기능을 계속 써야하니까 함수로
def vacation(L,P,V):
    #사용 기간 꽉채운 휴가일
    A = (V // P) * L 

    #사용 기간 안채운 휴가일
    if (V % P) <= L:
        B = V % P
    elif (V % P) > L:
        B = L
    return A+B

# L,P,V = (0,0,0) 일 때까지 무한 출력
i = 1
while True:
    L,P,V = map(int,input().split())
    # 입력값 0 0 0 일 때 중단
    if (L,P,V) == (0,0,0) :
        break
    #결과 출력
    print(f'Case {i}: {vacation(L,P,V)}')
    i += 1