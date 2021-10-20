from collections import deque 

n = int(input())
towers = [(n, i) for i, n in enumerate(list(map(int, input().split())), start=1)]
towers_deque = deque()
answer = []

for i in range(n):
    h, idx = towers[i]
    catch_idx = 0
    
    while(1):
        if not towers_deque:
            towers_deque.append((h, idx))
            break            
        elif towers_deque[-1][0] < h:
            towers_deque.pop()
        else:
            catch_idx = towers_deque[-1][1]
            towers_deque.append((h, idx))
            break          
        
    answer.append(catch_idx)

print(' '.join(map(str, answer)))