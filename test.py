n = int(input())
i = 1
number = 1
arr = [0] * n
for i in range(1, n + 1):
    for j in range(i):
        print(number, end=" ")
        arr[j] += number
        number += 1
    print('')
print(' '.join(map(str, arr)))