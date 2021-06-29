from itertools import permutations as p

def handle_exp(exp):
    operand = [] 
    operator = []
    tmp = ""
    for i in exp:
        if i.isdigit():
            tmp += i
        else:
            operand.append(int(tmp))
            tmp = ""
            operator.append(i)
    if tmp != "":
        operand.append(int(tmp))
    return [operand, operator]

def solution(expression):
    answer = 0
    priorities = list(p(["+", "-", "*"], 3))
    for prior in priorities:
        operand, operator = handle_exp(expression)
        for oper in prior:
            while(oper in operator):
                i = operator.index(oper)
                if oper == "+":
                    result = operand[i] + operand[i + 1]
                    del operand[i]
                    del operand[i]
                    del operator[i]
                    operand.insert(i, result)
                elif oper == "-":
                    result = operand[i] - operand[i + 1]
                    del operand[i]
                    del operand[i]
                    del operator[i]
                    operand.insert(i, result)
                else:
                    result = operand[i] * operand[i + 1]
                    del operand[i]
                    del operand[i]
                    del operator[i]
                    operand.insert(i, result)
        if operand[0] < 0:
            operand[0] = -operand[0]
        if answer < operand[0]:
            answer = operand[0]
    return answer