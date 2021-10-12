n = int(input())

number_stack = []
target_stack = []
seq = []
answer = []
for _ in range(n):
    seq.append(int(input()))

now_number = 1
cursor = 0
fail = False

while(len(target_stack) != n):
    while(now_number <= n):
        number_stack.append(now_number)
        now_number += 1
        answer.append('+')
        
        while(number_stack and number_stack[-1] == seq[cursor]):
            target_stack.append(number_stack.pop())
            cursor += 1
            answer.append('-')
        
    if now_number > n and number_stack and number_stack[-1] != seq[cursor]:
        print("NO")
        fail = True
        break

if not fail:
    for oper in answer:
        print(oper)