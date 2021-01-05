a, b = input().split()
num1 = []
num2 = []
for i in range(len(a) - 1, -1, -1):
    num1.append(a[i])
for i in range(len(b) - 1, -1, -1):
    num2.append(b[i])
num1 = int(''.join(num1))
num2 = int(''.join(num2))
print(max(num1, num2))