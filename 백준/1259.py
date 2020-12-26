while(True):
    number = input()
    if number == '0' :
        break
    length = len(number)
    answer = 'yes'
    for i in range(length // 2):
        if number[i] != number[-(i + 1)]:
            answer = 'no'
            break
    print(answer) 