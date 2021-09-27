n = int(input())
five = n // 5

# 5원짜리 동전을 최대한 써보는데 안되면 하나씩 줄여보기
while(five >= 0):
    tmp = n
    tmp -= five * 5
    if tmp % 2 != 0:
        five -= 1
    else:
        print(five + tmp // 2)
        break

if five == -1:
    print(-1)
