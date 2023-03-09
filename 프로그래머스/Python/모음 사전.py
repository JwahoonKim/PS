from itertools import product


def solution(word):
    m = ['A', 'E', 'I', 'O', 'U']

    words = []
    for i in range(1, 6):
        for w in map(lambda x: ''.join(x), list(product(m, repeat = i))):
            words.append(w)

    words.sort()

    return words.index(word) + 1

print(solution('AAAAE'))