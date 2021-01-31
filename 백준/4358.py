from collections import Counter
import sys

input = sys.stdin.readline

trees = []
# trees의 length
length = 0
while 1:
    tree = input()
    if tree == "\n":
        break
    else:
        trees.append(tree.rstrip())
        length += 1

counter = Counter(trees)
counter = sorted(counter.items())

for treeInfo in counter:
    treeName = treeInfo[0]
    count = treeInfo[1]
    print(treeName, round(100 * count / length, 4))
