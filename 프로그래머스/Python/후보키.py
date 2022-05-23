from itertools import combinations as c

def solution(relation):
    keys = []
    for i in range(1, len(relation[0]) + 1):
        col_comb = c(list(range(len(relation[0]))), i)
        for comb in col_comb:
            now = []
            for row in range(len(relation)):
                key = []
                for col in comb:
                    key.append(relation[row][col])
                if key in now:
                    break
                now.append(key)
                if row == len(relation) - 1:
                    if not keys:
                        keys.append(comb)
                    now = set(comb)
                    for i in range(len(keys)):
                        k = set(keys[i])
                        if k.issubset(now):
                            break
                        else:
                            if i == len(keys) - 1:
                                keys.append(comb)
    return len(keys)