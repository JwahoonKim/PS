import sys

input = sys.stdin.readline

# 입력받기
n = int(input())
arr = []
for _ in range(n):
    name, kor, eng, math = input().split()
    arr.append((name, int(kor), int(eng), int(math)))

# 조건에 따라 정렬
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 출력
for i in arr:
    print(i[0])