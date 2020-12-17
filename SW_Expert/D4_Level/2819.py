# 시작점 총 16개 (4 X 4)
# 상하좌우 선택 (4가지) 를 총  6번 ( 4^6 가지)
# 문자열로 붙인 다음 배열에 추가 (이미 있다면 추가 X)
# 배열의 길이 == 답
def make_str(x, y, string):
    if len(string) == 7:
        if string not in arr:
            arr.append(string)
    