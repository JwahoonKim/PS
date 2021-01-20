a = [[1,2,3],[4,5,6],[3,100,100]]
b = set()
for i in a:
    for j in i:
        b.add(j)
b = sorted(b, reverse=True)
print(b)