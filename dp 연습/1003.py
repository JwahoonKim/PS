t = int(input())
arr =[]
for i in range(t):
    arr.append(int(input()))

zero = [1, 0]
one  = [0, 1]

for j in range(2, max(arr)+1):
    zero.append(sum(zero[-2:]))
    one. append(sum(one [-2:]))

for k in arr:
    print(zero[k], one[k])