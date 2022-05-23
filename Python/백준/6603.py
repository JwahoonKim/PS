def combination(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result

while 1:
    s = list(map(int, input().split(' ')))
    if s == [0]:
        break
    k = s[0]
    s = s[1:]
    comb = combination(s, 6)
    for c in comb:
        print(' '.join(map(str, c)))
    print('')
