a, b = map(int, input().split())
div = min(a, b)

while 1:
    if a % div == 0 and b % div == 0:
        break
    div -= 1

G = div
L = G * (a // div) * (b // div)
print(G)
print(L)