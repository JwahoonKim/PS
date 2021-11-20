from bisect import bisect_left
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
titles = []
powers = []

for _ in range(n):
    title, power = input().rstrip().split()
    titles.append(title)
    powers.append(int(power))

for _ in range(m):
    cur_power = int(input())
    # bisect_left => 이분탐색해서 두번째 인자 값이 들어갈 위치(동일 값 존재시 배열의 왼쪽으로 삽입 기준) idx를 반환함
    idx = bisect_left(powers, cur_power)
    print(titles[idx])
