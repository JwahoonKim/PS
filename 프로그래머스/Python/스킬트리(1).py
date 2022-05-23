def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        skill_tree = skill_trees[i]
        flag = False
        for j in range(len(skill) - 1):
            # 해당 스킬이 있는 경우, 그 위치 앞쪽에는 다음에 배울 스킬이 없어야됨
            if skill[j] in skill_tree:
                place = skill_tree.index(skill[j])
                for k in skill[j + 1:]:
                    if k in skill_tree[:place]:
                        flag = True
                        break
            if flag == True:
                break    
            # 해당 스킬이 없는 경우 그 다음에 배울 스킬은 하나도 없어야됨
            elif skill[j] not in skill_tree:
                for k in skill[j + 1:]:
                    if k in skill_tree:
                        flag = True
                        break
                if flag == True:
                    break
        if flag == False:
            answer += 1
    return answer



skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))