import copy 

def solution(n, lost, reserve):
    arr = copy.deepcopy(reserve)
    for i in reserve:
        if i in lost:
            lost.remove(i)
            arr.remove(i)
    for j in arr:
        if j in lost:
            lost.remove(j)
        elif j - 1 in lost:
            lost.remove(j - 1)
        elif j + 1 in lost:
            lost.remove(j + 1)
    return n - len(lost)