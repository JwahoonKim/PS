T = int(input())
for test_case in range(1, T + 1):
    month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = 0
    month1, day1, month2, day2 = map(int, input().split())
    if month1 == month2:
        ans = day2 - day1 + 1
    else:
        ans += day[month1] - day1 + 1
        for i in range(month1 + 1, month2):
            ans += day[i]
        ans += day2
    print(f'#{test_case} {ans}')

