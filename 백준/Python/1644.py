N = int(input())

isPrime = [False] * 2 + [True] * (N - 1)
primeNumbers = []

for n in range(2, N + 1):
    if isPrime[n]:
        primeNumbers.append(n)
        for k in range(2 * n, N + 1, n):
            isPrime[k] = False

answer = 0
left = 0
right = 0
sum = primeNumbers[0] if N != 1 else 0

if N != 1:
    while 1:
        if sum == N:
            answer += 1
            right += 1
            if right == len(primeNumbers):
                break
            sum += primeNumbers[right]
        elif sum < N:
            right += 1
            if right == len(primeNumbers):
                break
            sum += primeNumbers[right]
        else:
            sum -= primeNumbers[left]
            left += 1
            if left == len(primeNumbers):
                break

print(answer)
