def isSequence(n):
    number = str(n)
    length = len(number)
    if length == 1:
        return True
    d = int(number[0]) - int(number[1])
    for i in range(length - 1):
        if int(number[i]) - int(number[i + 1]) != d:
            return False
    return True        

if __name__ == "__main__":
    n = int(input())
    count = 0 
    numbers = [i + 1 for i in range(n)]
    for num in numbers:
        if isSequence(num):
            count += 1
    print(count)