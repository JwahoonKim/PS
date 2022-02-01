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
    isHead = False
    for c in file:
        if c.isdigit():
            isHead = True
            res += c
        elif isHead:
            break
    return int(res)

def solution(files):
    answer = sorted(files, key = lambda x : (getHead(x), getNumber(x)))
    return answer