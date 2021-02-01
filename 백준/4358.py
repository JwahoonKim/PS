from collections import Counter
import sys

input = sys.stdin.readline

trees = dict()
countTotalTree = 0

while 1:
    tree = input()
    if tree == "\n":
        break
    tree = tree.rstrip()
    if tree in trees:
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
    print(treeName, round(100 * countTree / countTotalTree, 4))
