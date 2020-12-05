N = int(input())
arr = []

def check(num):
    result = ""
    numToString = str(num)
    for i in numToString:
        if int(i) != 0 and int(i) % 3 == 0:
            result += '-'
    return result

for i in range(1, N + 1):
    num = check(i)
    if num == '':
        arr.append(i)
    else :
        arr.append(num)

for i in range(len(arr)):
    print(arr[i], end = " ")