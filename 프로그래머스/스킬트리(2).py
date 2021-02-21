def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skilList = list(skill)
        skill_treeList = list(skill_tree)
        # skill_tree에서 확인할 필요없는 스킬들은 다 없앤 배열
        cleanTree = [i for i in skill_treeList if i in skilList]
        while(1):
            if len(cleanTree) == 0:
                answer += 1
                break
            skillPointer = skilList.pop(0)
            TreePointer = cleanTree.pop(0)
            if skillPointer != TreePointer:
                break
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))