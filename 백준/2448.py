n = int(input())
stars = ['  *  ',' * * ', '*****']
shift = 3
while n > 3:
    for i in range(len(stars)):
        # 위에 별 모양 두개 복사
        stars.append(stars[i] + ' ' + stars[i]) 
        # 위에 별 밀어주기
        stars[i] = ' ' * shift + stars[i] + ' ' * shift 
    n //= 2
    shift *= 2

for s in stars:
    print(s)