N, K = map(int, input().split())
people = list(range(1, N + 1))
cursor = 0
numbers = []

while(people):
    cursor = (cursor + K - 1) % len(people)
    numbers.append(people.pop(cursor))

print('<'+', '.join(map(str, numbers))+'>')