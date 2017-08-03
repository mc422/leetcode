# -*- coding: utf-8 -*-
# 473. Matchsticks to Square

# wrong solution
def makesquare(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 4:
        return False

    sum = 0
    for i in nums:
        sum += i

    if sum % 4 != 0:
        return False

    edge = sum / 4
    nums.sort()

    if nums[-1] > edge:
        return False

    count = 0
    visited = [False for i in range(len(nums))]

    def dfs(i, cur, target, visited):
        if visited[i]:
            return False
        if cur + nums[i] > target:
            return False
        visited[i] = True
        cur += nums[i]
        if cur == target:
            return True
        else:
            j = i+1
            while j < len(nums):
                if dfs(j, cur, target, visited):
                    return True
                j += 1
            visited[i] = False
            return False

    for i in range(len(nums)):
        if dfs(i, 0, edge, visited):
            count += 1

    if count == 4:
        return True
    else:
        return False


def makesquare2(nums):
    sums = sum(nums)
    if sums % 4 != 0:
        return False
    target = sums / 4
    nums.sort()

    each = [0 for i in range(4)]
    def helper(nums, pos, each, target, visited):
        if pos == len(nums):
            return each[0] == target and each[1] == target and each[2] == target

        state = tuple(sorted(each))  # 通过给sums排序，可以固定出唯一的状态
        if state in visited: return False

        for i in range(4):
            if each[i] + nums[pos] > target:
                continue
            each[i] += nums[pos]
            if helper(nums, pos+1, each, target, visited):
                return True
            each[i] -= nums[pos]
        visited.add(state)
        return False
    states = set()
    return helper(nums, 0, each, target, states)


test = [1,1,1,1,2,2,2,2]

print makesquare2(test)
