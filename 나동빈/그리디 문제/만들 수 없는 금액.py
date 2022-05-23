N = input()
coin = list(map(int, input().split())) # 1 2 3/  5 7 
coin.sort()
target = 1
for x in coin:
    if target < x:
        break
    else: 
       target += x 
print(target)