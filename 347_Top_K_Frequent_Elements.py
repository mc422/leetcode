# 347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# solution 1: use bucketSort to find the top K fequency
import collections
import heapq


class Solution(object):
    def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)
        cnt = collections.defaultdict(int)
        for num in nums:
            cnt[num] += 1
        buckets = [[] for i in range(l + 1)]
        for key, val in cnt.iteritems():
            buckets[val].append(key)

        ans = []
        for i in range(l, -1, -1):
            ans += buckets[i]

        return ans[:k]


# solution 2: use heap
class Solution2(object):
    def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)
        cnt = collections.defaultdict(int)
        for num in nums:
            cnt[num] += 1

