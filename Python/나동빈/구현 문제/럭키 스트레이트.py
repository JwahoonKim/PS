n = list(map(int, input()))
length = len(n)
sum1 = sum(n[0 : length // 2]) 
sum2 = sum(n[length // 2 : ])

if sum1 == sum2 :
    print("LUCKY")
else: 
    print("READY")