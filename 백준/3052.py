numbers = []
numset = set()
for i in range(10):
    numbers.append(int(input()))
for i in range(10):
    numset.add(numbers[i] % 42)
print(len(numset))