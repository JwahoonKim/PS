from collections import deque
import heapq


def solution(priorities, location):
    answer = 0
    cur = 0
    count = 0
    printer = deque() 
    for i in range(len(priorities)):
        printer.append([priorities[i], i])
    priorities.sort(reverse=True)
    
    while(1):
        now = priorities[cur]
        prior, locate = printer.popleft()
        
        if prior != now:
            printer.append([prior, locate])
        elif prior == now:
            cur += 1
            count += 1
            if locate == location:
                return count
    return answer



print(solution([2, 1, 3, 2], 2))

