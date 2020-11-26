n = int(input())
s1 = n // 5 

while(True):
    r1 = n - (5*s1)
    if r1 % 3 == 0 :
        ans = s1 + (r1 // 3)
        break
    else: s1 = s1 - 1
    if s1 == -1:
        break
    
print(ans)    