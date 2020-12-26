a, b = map(int, input().split())
div = min(a, b)
G = 1
L = a * b
while(div != 1):
    if a % div == 0 and b % div == 0:
        G *= div
        L = G * (a // div) * (b // div)
        break
    else: 
        div -= 1
print(G)
print(L)