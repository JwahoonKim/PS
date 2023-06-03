from collections import deque

T = int(input())

for _ in range(T):
    commands = input()
    n = int(input())
    nums = deque(input()[1:-1].split(','))

    if n == 0:
        nums = deque()

    REVERSED = False
    ERROR = False

    for cmd in commands:
        if cmd == 'R':
            REVERSED = not REVERSED

        if cmd == 'D':
            if not nums:
                ERROR = True
                break
            if REVERSED:
                nums.pop()
            else:
                nums.popleft()

    if ERROR:
        print("error")
    elif REVERSED:
        print('[' + ','.join(list(nums)[::-1]) + ']')
    else:
        print('[' + ','.join(nums) + ']')
