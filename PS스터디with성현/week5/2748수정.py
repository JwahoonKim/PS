n = int(input())
d = [0] * 91
d[1] = 1

for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])


# n = int(input())
# fibo = [0,1]

# for i in range(2, n + 1):
#     next = fibo[i - 1] + fibo[i - 2]
#     fibo.append(next)

# print(fibo[n])
