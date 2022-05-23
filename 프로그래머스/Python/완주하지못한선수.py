def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] == completion[i]:
            continue
        else:
            return participant[i]
    return participant[len(participant) - 1]