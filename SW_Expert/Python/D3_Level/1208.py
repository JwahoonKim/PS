T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(dump):
        max_value = max(box)
        min_value = min(box)
        if max_value == min_value:
            break
        max_index = box.index(max_value)
        min_index = box.index(min_value)
        box[max_index] -= 1
        box[min_index] += 1
    ans = max(box) - min(box)
    print(f'#{test_case} {ans}')