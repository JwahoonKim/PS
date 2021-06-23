def solution(s):
    alps = []
    for alp in s:
        if len(alps) == 0 or alps[-1] != alp:
            alps.append(alp)
        else:
            alps.pop()
    if len(alps) == 0:
        return 1
    else:
        return 0
