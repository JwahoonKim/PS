from itertools import combinations as c

n, k = map(int, input().split())

mustKnow = ["a", "c", "n", "t", "i"]
alpList = [
    "b",
    "d",
    "e",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "u",
    "v",
    "w",
    "y",
    "z",
]
teachList = []
answer = 0

if k < 5:
    for _ in range(n):
        input()
    print(0)
else:
    for _ in range(n):
        # 입력에서 a,c,n,t,i는 뺀 나머지 알파벳만 삽입
        word = list(
            set((filter(lambda x: x not in mustKnow, list(map(str, input().rstrip())))))
        )
        teachList.append(word)
    alpComb = list(c(alpList, k - 5))

    for case in alpComb:
        count = 0
        flag = True
        for teach in teachList:
            for k in teach:
                if k in case:
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                count += 1
            else:
                flag = True
        answer = max(answer, count)
    print(answer)

print(teachList)
print(alpComb)