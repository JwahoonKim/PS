n = int(input())
#DP table
d = [0] * 91
# d 가 fibo 함수 안에서도 쓰임?

def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(n))
