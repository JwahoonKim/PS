T = int(input())
zero = [1, 0]
one = [0, 1]

for i in range(2, 41):
    zero.append(sum(zero[-2:]))
    one.append(sum(one[-2:]))

for _ in range(T):
    n = int(input())
    print(zero[n], one[n])

