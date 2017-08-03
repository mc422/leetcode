# 332. Reconstruct Itinerary
from collections import defaultdict

import collections


def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """

    def dfs(cur, dests, ans, counter):
        if counter == len(tickets)+1:
            return True
        cur_dests = dests.get(cur)
        for idx, val in enumerate(cur_dests):
            ans.append(val)
            del cur_dests[idx]
            if dfs(val, dests, ans, counter+1):
                return True
            ans.pop()
            cur_dests.insert(idx, val)
        return False

    dests = defaultdict(list)
    for ticket in tickets:
        dests[ticket[0]].append(ticket[1])

    for src, dest in dests.iteritems():
        dest.sort()

    start = 'JFK'
    ans = [start]
    if dfs(start, dests, ans, 1):
        return ans
    else:
        return []

# http://bookshadow.com/weblog/2016/02/05/leetcode-reconstruct-itinerary/
def findItinerary2(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    routes = defaultdict(list)
    for s, e in tickets:
        routes[s].append(e)

    def solve(start):
        left, right = [], []
        for end in sorted(routes[start]):
            if end not in routes[start]:
                continue
            routes[start].remove(end)
            subroutes = solve(end)
            if start in subroutes:
                left += subroutes
            else:
                right += subroutes
        return [start] + left + right

    return solve("JFK")


def findItinerary3(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route = []
    def visit(airport):
        # route.append(airport)
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)
    visit('A')
    return route[::-1]


test = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
test2 = [["JFK","A"], ['A', 'X'], ['X', 'Y'], ['Y', 'A'], ['A', 'B'], ['B', 'D']]
test3 = [["A","B"], ['B', 'C'], ['C', 'X'], ['X', 'A'], ['A', 'B'], ['B', 'C'], ['C', 'D']]
print sorted(test2)
print findItinerary3(test3)
