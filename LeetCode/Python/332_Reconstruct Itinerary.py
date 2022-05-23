from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        ticket_dict = defaultdict(list)

        for ticket in tickets:
            ticket_dict[ticket[0]].append(ticket[1])

        for key in ticket_dict:
            ticket_dict[key].sort(reverse=True)


        def dfs(start):
            while ticket_dict[start]:
                next = ticket_dict[start].pop()
                dfs(next)
            answer.append(start)

        dfs("JFK")

        return answer[::-1]

