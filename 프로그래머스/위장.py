def solution(clothes):
    answer = 1
    dictionary = dict()
    for cloth in clothes:
        name, cloth_type = cloth
        if cloth_type in dictionary:
            dictionary[cloth_type].append(name)
        else:
            dictionary[cloth_type] = [name]
    for now in dictionary.values():
        answer *= (len(now) + 1)
    return answer - 1
