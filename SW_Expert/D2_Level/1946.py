T = int(input())
for test_case in range(1, T + 1):
    
    N = int(input())
    alp_arr = []
    num_arr = []
    count = 0
    for i in range(N):
        count = 0
        alp, num = input().split()
        num = int(num)
        alp_arr.append(alp)
        num_arr.append(num)
    print(f'#{test_case}')
    for i in range(N):  
        a = alp_arr[i]
        num = num_arr[i]
        for j in range(num):
            print(a, end ="")
            count += 1
            if count == 10:
                print("")
                count = 0
    