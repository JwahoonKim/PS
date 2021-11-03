import re 

T = int(input())

for _ in range(T):
    if re.match(r'[A-F]?A+F+C+[A-F]?$', input()):
        print('Infected!')
    else:
        print('Good')