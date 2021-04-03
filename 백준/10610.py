numList = sorted(list(map(int, input())), reverse=True)

# 30의 배수를 만들지 못하는 조건
if 0 not in numList or sum(numList) % 3 != 0:
    print(-1)
else:
    print(int(''.join(map(str, numList))))
