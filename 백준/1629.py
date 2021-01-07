a, b, c = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % c
    else:
        half = power(a, b // 2)
        if b % 2 == 0:
            return half * half % c
        else:
            return a * half * half % c
print(power(a,b))
