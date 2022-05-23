def solution(numbers):
    arr = []
    leng = len(numbers)
    for i in range(leng):
        for j in range(leng):
            if i == j:
                continue
            result = numbers[i] + numbers[j]
            count = 0
            for check in arr:
                if check == result:
                    count += 1
            if count == 0:
                arr.append(result)
    return sorted(arr)

arr1 = [1,2,3,4]
sol1 =solution(arr1)

print(sol1)