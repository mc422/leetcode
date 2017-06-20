def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    nexts = [set() for i in range(numCourses)]
    for pre in prerequisites:
        nexts[pre[1]].add(pre[0])

    require_nums = [0 for i in range(numCourses)]
    stack = [i for i in range(numCourses)]
    for pre in prerequisites:
        require_nums[pre[0]] += 1
        if pre[0] in stack:
            stack.remove(pre[0])

    ans = []
    while stack:
        print stack
        cur = stack.pop()
        ans.append(cur)
        for next in nexts[cur]:
            require_nums[next] = require_nums[next] - 1
            if require_nums[next] == 0:
                stack.append(next)

    if len(ans) == numCourses:
        return ans
    else:
        return []


list = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
print findOrder(len(list), list)