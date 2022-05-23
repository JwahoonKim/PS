T = int(input())
for test_case in range(1, T + 1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    N = int(input())
    for i in range(8):
        count[i] += N // money[i]
        N -=  money[i] * (N // money[i])
    print(f"#{test_case}")
    for i in count:
        print(i, end = " ")
    print("")
