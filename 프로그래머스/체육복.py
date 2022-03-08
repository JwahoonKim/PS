def solution(n, lost, reserve):
    # 도난 + 여벌 학생 지우기
    _lost = sorted([i for i in lost if i not in reserve])
    _reserve = sorted([i for i in reserve if i not in lost])
    
    # 여벌 체육복 빌려주기
    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)
            
    return n - len(_lost)