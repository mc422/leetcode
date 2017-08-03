# 638. Shopping Offers
import sys


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        # if all([True for n in needs if n == 0]):
        #     return 0
        l = len(needs)
        best = sys.maxint
        for s in special:
            new_needs = list(needs)
            fit = True
            for i in range(l):
                if new_needs[i] >= s[i]:
                    new_needs[i] -= s[i]
                else:
                    fit = False
            if fit:
                after = self.shoppingOffers(price, special, new_needs)
                best = min(after + s[-1], best)
        single = 0
        for i in range(l):
            single += price[i] * needs[i]
        return min(single, best)


# recursion with memorization
def best_price(price, special, needs, need_map):
    l = len(needs)
    if tuple(needs) in need_map:
        return need_map.get(tuple(needs))
    best = 0
    for i in range(l):
        best += price[i] * needs[i]
    for s in special:
        new_needs = list(needs)
        fit = True
        for i in range(l):
            if new_needs[i] >= s[i]:
                new_needs[i] -= s[i]
            else:
                fit = False
        if fit:
            after = best_price(price, special, new_needs, need_map)
            best = min(after + s[-1], best)
    need_map[tuple(needs)] = best
    return best

p = [2,5]
s = [[3,0,5],[1,2,10]]
n = [3,2]

sl = Solution()
print sl.shoppingOffers(p, s, n)