from collections import deque

# 첫 풀이
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

# 두 번째 풀이
def solution(priorities, target):
    prior_index = deque(list(enumerate(priorities)))
    prior_sorted = deque(sorted(priorities, reverse=True))
    count = 1
    while(prior_sorted):
        # 우선순위가 더 높은게 있다면
        if prior_index[0][1] != prior_sorted[0]:
            prior_index.append(prior_index.popleft())
        else:
            prior_sorted.popleft()
            if prior_index[0][0] == target:
                return count
            else:
                count += 1
                prior_index.popleft()
