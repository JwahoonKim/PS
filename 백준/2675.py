T = int(input())

for i in range(T):
    num, word = input().split()
    num = int(num)
    for i in word:
        print(i * num, end = '')
    print('')
