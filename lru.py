class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.cache = []

    def get(self, key):
        """
        :rtype: int
        """
        val = self.dict.get(key)
        if not val:
            return -1
        else:
            self.reset(key)
            return val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        val = self.dict.get(key)
        if val:
            self.dict[key] = value
            self.reset(key)
        else:
            if self.size < self.capacity:
                self.dict[key] = value
                self.size += 1
                self.reset(key)
            else:
                least_key = self.cache[self.size - 1]
                self.cache.remove(self.size - 1)
                del self.dict[least_key]
                self.dict[key] = value
                self.reset(key)

    def reset(self, key):
        if key in self.cache:
            self.cache.remove(key)
        self.cache.insert(0, key)

test = LRUCache(1)
test.set(2, 1)
test.get(2)
test.set(3,2)