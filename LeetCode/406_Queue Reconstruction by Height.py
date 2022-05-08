from collections import deque

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people.sort(key=lambda x:(x[0], -x[1]), reverse=True)
        q = deque(people)
        
        while q:
            person = q.popleft()
            result.insert(person[1], person)

        return result

