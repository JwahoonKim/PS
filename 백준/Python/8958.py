T = int(input())
for i in range(T):
    result = input()
    score = 0
    flag = 1
    for ox in result:
        if ox == 'O':
            score += flag
            flag += 1
        elif ox == 'X':
            flag = 1
    print(score)