# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
#
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.
#
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other words,
# you can't store all numbers coming from the stream as it's too large to hold in memory.
# Could you solve it efficiently?


def findMaxConsecutiveOnes(nums):
    ans = 0
    cnt, prev = 0, 0
    for i in nums:
        cnt += 1
        if i == 0:
            prev = cnt
            cnt = 0
        ans = max(ans, prev+cnt)
    return ans

print findMaxConsecutiveOnes([0,0,1,1,0,0,1,1,1,0,1])


# what is we want to flip k number of 0s. The way is to maintain a windows
# that has k 0s.

# what if the data flow is a stream and we want look back data?
# we can

def findMaxConsecutiveOnes2(nums, k):
    j = 0
    ans = 0
    cnt = 0
    l = []
    for i in range(len(nums)):
        cnt += 1
        if nums[i] == 0:
            l.append(i)
        if len(l) > k:
            loc = l[0]
            del l[0]
            cnt -= (loc-j+1)
            j = loc + 1
        ans = max(ans, cnt)
    return ans

print findMaxConsecutiveOnes2([0,0,1,1,0,0,1,1,1,0,1], 2)