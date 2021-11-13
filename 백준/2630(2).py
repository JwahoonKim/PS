n = int(input())
white = 0
blue = 0
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

def isBlue(arr):
    for a in arr:
        if 0 in a:
            return False
    return True

def isWhite(arr):
    for a in arr:
        if 1 in a:
            return False
    return True

# 4등분으로 종이 잘라서 리턴
def cut_paper(arr):
    n = len(arr)
    paper1 = []
    paper2 = []
    paper3 = []
    paper4 = []
    for i in range(n // 2):
        paper1.append(arr[i][:n // 2])
        paper2.append(arr[i][n // 2:])
    for i in range(n // 2, n):
        paper3.append(arr[i][:n // 2])
        paper4.append(arr[i][n // 2:])
    return [paper1, paper2, paper3, paper4]

def check(arr):
    global white, blue
    if isBlue(arr):
        blue += 1
        return
    if isWhite(arr):
        white += 1
        return
    cutted_papers = cut_paper(arr)
    for cutted_paper in cutted_papers:
        check(cutted_paper)

check(paper)
print(white)
print(blue)