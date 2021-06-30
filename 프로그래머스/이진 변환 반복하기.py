def solution(s):
    count = 0
    del_zero = 0
    while(s != '1'):
        after = ""
        count += 1
        for i in s:
            if i == '0':
                del_zero += 1
            else:
                after += i
        s = to_binary(len(after))
    return [count, del_zero]


def to_binary(length):
    return str(format(length, 'b'))
