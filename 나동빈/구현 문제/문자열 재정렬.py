n = input()
right = []
left = 0
for check in n:
    if check in '1234567890':
        left += int(check)
    else:
        right.append(check)
right.sort()
ans = ''.join(right) + str(left)
print(ans)
