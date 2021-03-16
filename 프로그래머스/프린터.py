from collections import deque


def solution(priorities, target):
    cur = 0
    count = 0
    printer = deque()
    for i in range(len(priorities)):
        printer.append([priorities[i], i])
    priorities.sort(reverse=True)

    while 1:
        highestPrior = priorities[cur]
        prior, location = printer.popleft()
        # 더 높은 우선순위가 존재하면 뒤에 다시 붙여
        if prior != highestPrior:
            printer.append([prior, location])
        elif prior == highestPrior:
            cur += 1
            count += 1
            if location == target:
                return count
