# 380. Insert Delete GetRandom O(1)
#
# first, to find value with O(1), you need a hashtable
# second, to randomly select an element with O(1), you need a list so you can randomly choose index
#  and get the element
# So the solution is a hashtabe and a array
# when we remove one element, we copy the last one into it.
import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.nums = []
        self.index = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.nums.append(val)
            self.map[val] = self.index
            self.index += 1
            # print self.map, self.nums
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            loc = self.map[val]
            last = self.nums[-1]
            self.map[last] = loc
            self.nums[loc] = last
            self.nums[-1] = val
            self.map.pop(val)
            self.nums.pop()
            self.index -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, self.index - 1)]
