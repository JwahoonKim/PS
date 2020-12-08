def solution(participant, completion):
    part = sorted(participant)
    comp = sorted(completion)
    ans = ""
    for i in range(len(comp)):
        if part[i] != comp[i]:
            if part[i + 1] == comp[i]:
                ans = part[i]
                break         
    if ans == "":
        ans = part[-1]
    return ans