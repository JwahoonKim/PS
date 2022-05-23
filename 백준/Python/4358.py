import sys

input = sys.stdin.readline

trees = dict()
countTotalTree = 0

while 1:
    tree = input().rstrip()
    if not tree:
        break
    if trees.get(tree):
        trees[tree] += 1
        countTotalTree += 1
    else:
        trees[tree] = 1
        countTotalTree += 1

sortedTrees = sorted(trees.items())

# 정답 출력
for treeInfo in sortedTrees:
    treeName = treeInfo[0]
    countTree = treeInfo[1]
    print(treeName, "%.4f" % round(100 * countTree / countTotalTree, 4))
