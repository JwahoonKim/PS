from typing import List


def find(city, parent):
    if parent[city] == city:
        return city
    parent[city] = find(parent[city], parent)
    return parent[city]


def union(a_city, b_city, parent):
    a_parent = find(a_city, parent)
    b_parent = find(b_city, parent)
    if a_parent == b_parent:
        return
    parent[b_parent] = a_parent



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected[0]))]
        for cur_city, connections in enumerate(isConnected):
            for next_city, is_connected in enumerate(connections):
                if is_connected and cur_city != next_city:
                    union(cur_city, next_city, parent)

        answer = set()
        for i, p in enumerate(parent):
            if i == p:
                answer.add(i)

        return len(answer)

