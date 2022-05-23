import sys
input = sys.stdin.readline

def permutation(word, now):
    if word == "":
        anagramSet.add(now)
        return
    for i in range(len(word)):
        elem = word[i]
        permutation(word[:i] + word[i+1:], now + elem)

n = int(input())

for _ in range(n):
    word = input().rstrip()
    anagramSet = set()
    permutation(word, "")
    result = sorted(anagramSet)
    for r in result:
        print(r)
