N = int(input())
data = list(map(int, input().split()))
data.sort()
people = 0 
group = 0
for cur in data:
    people += 1
    if cur == people:
        group += 1
        people = 0
print(group)
