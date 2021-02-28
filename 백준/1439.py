string = str(input())
count = 0
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        count += 1
if count % 2 == 0:
    print(count // 2)
else:
    print(count // 2 + 1)
