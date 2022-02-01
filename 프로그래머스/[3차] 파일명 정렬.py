def getHead(file):
    res = ""
    for c in file:
        if c.isdigit():
            break
        else:
            res += c
    return res.lower()

def getNumber(file):
    res = ""
    isTail = False
    for c in file:
        if c.isdigit():
            isTail = True
            res += c
        elif isTail:
            break
    return int(res)

def solution(files):
    answer = sorted(files, key = lambda x : (getHead(x), getNumber(x)))
    return answer