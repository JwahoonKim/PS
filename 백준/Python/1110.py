n = int(input())
cycle = 0
now = n
while(1):
    cycle += 1
    next = int(str(now % 10) + str(((now // 10) + (now % 10)) % 10))
    if n == next:
        break
    now = next
print(cycle)
