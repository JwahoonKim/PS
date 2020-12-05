T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score = [0]
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    cut = N / 10 
    for i in range(N):
        a, b, c = map(int, input().split())
        total = a * 0.35 + b * 0.45 + c * 0.2
        score.append(total)
    target = score[K]
    score.sort(reverse = True)
    rank = score.index(target) // cut
    print(f'#{test_case} {grade[int(rank)]}' )
