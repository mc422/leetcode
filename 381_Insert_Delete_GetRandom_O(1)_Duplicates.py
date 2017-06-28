import random
from collections import defaultdict


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(list)
        self.nums = []
        self.index = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        contains = False if val in self.table else True
        self.table[val].append(self.index)
        self.nums.append(val)
        self.index += 1
        return contains

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.table:
            loc = self.table[val].pop()
            last = self.nums[self.index - 1]
            print val, loc, last, self.nums, self.table
            if loc == self.index - 1:
                self.nums.pop()
            else:
                self.nums[loc] = last
                self.table[last].remove(self.index - 1)
                self.table[last].append(loc)
                self.nums.pop()
            self.index -= 1
            if not self.table[val]:
                del self.table[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.nums[random.randint(0, self.index- 1)]