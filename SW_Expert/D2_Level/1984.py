
T = int(input())
for test_case in range(1, T + 1):
    numlist = list(map(int, input().split()))
    maxi = max(numlist)
    mini = min(numlist)
    numlist.remove(maxi)
    numlist.remove(mini)
    ans = round(sum(numlist) / 8)
    print(f'#{test_case} {ans}')