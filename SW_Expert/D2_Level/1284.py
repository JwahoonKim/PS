T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    cost1 = W * P
    if W <= R:
        cost2 = Q
    else:
        cost2 = Q + (W - R) * S
    cost = min(cost1, cost2)
    print(f'#{test_case} {cost}')