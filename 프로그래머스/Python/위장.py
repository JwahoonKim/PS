def solution(clothes):
    answer = 1
    dictionary = {}
    for c, t in clothes:
        print(dictionary)
        if t not in dictionary:
            dictionary[t] = 2
        else:
            dictionary[t] += 1
    for num in dictionary.values():
        answer *= num
    return answer - 1
