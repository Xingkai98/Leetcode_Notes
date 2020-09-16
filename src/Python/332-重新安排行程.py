class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        return self.subFind(['JFK'], tickets)

    def subFind(self, current: List[str], tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return current
        right = current[-1:][0]
        nominee = sorted([i[1] for i in tickets if i[0] == right])
        if not nominee:
            return []
        for each in nominee:
            remain = tickets.copy()
            remain.remove([right, each])
            tmp = self.subFind(current + [each], remain)
            if tmp:
                return tmp