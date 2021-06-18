def count_change(alp):
    if alp >= 'N':
        return ord('Z') - ord(alp) + 1
    else:
        return ord(alp) - ord('A')


def solution(name):
    answer = 0
    cursor = 0
    visited = [False] * len(name)

    if name[0] != 'A':
        visited[0] = True
        answer += count_change(name[0])

    # A인곳은 갈 필요없어
    for i in range(len(name)):
        if name[i] == 'A':
            visited[i] = True

    while(not all(visited)):
        dist = 1
        while(1):
            if name[cursor + dist] != 'A' and visited[cursor + dist] == False:
                answer += count_change(name[cursor + dist]) + dist
                cursor += dist
                visited[cursor] = True
                break
            elif name[cursor - dist] != 'A' and visited[cursor - dist] == False:
                answer += count_change(name[cursor - dist]) + dist
                cursor -= dist
                visited[cursor] = True
                break
            else:
                dist += 1
    return answer