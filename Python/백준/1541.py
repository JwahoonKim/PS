exp = input().split('-')
ans = 0
for number in exp[0].split('+'):
    ans += int(number)
for j in exp[1:]:
    for number in j.split('+'):
        ans -= int(number)
print(ans)