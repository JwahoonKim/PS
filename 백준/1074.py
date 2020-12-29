n, r, c = map(int, input().split())
divide = [2 ** i for i in range(1, n)]
divide.sort(reverse=True)
number = 0
for i in divide:
    if r // i != 0:
        r %= i
        number += i ** 2 * 2
    if c // i != 0:
        c %= i
        number += i ** 2
if (r, c) == (0, 0):
    number += 0
elif (r, c) == (0, 1):
    number += 1
elif (r, c) == (1, 0):
    number += 2
elif (r, c) == (1, 1):
    number += 3

print(number)