def solution(n, words):
    pre = words[0]
    for i in range(1, len(words)):
        if words[i] in words[:i]:
            break
        elif pre[-1] != words[i][0]:
            break
        else:
            pre = words[i]
            if i == len(words) - 1:
                return [0, 0]
    person = (i % n) + 1
    rotate = (i // n) + 1
    return [person, rotate]
