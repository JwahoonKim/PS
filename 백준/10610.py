list = sorted(list(map(int, input())))
# 30의 배수를 만들지 못하는 조건
print("123".split(''))
if 0 not in list or sum(list) % 3 != 0:
    print(-1)
else:
    length = len(list)
    # 주어진 길이로 만들 수 있는 30의 배수 중 최대 값
    # ex.) len --> 4  --> 9990
    maxNumber = ""
    for _ in range(length - 1):
        maxNumber += '9'
    maxNumber = (maxNumber + '0')
    number = maxNumber

    while(int(number) >= 10 ** (length - 1)):
        numList = sorted(list(number))
        if numList == list:
            break
        number = str(int(number) - 30)

    print(number)
