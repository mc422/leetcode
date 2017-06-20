def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    connections = [set() for i in range(numCourses)]
    for i in range(len(prerequisites)):
        connections[prerequisites[i][1]].add(prerequisites[i][0])

    in_degrees = [0 for i in range(numCourses)]
    stack = [i for i in range(numCourses)]
    for i in range(numCourses):
        connection = connections[i]
        for j in connection:
            in_degrees[j] += 1
            if j in stack:
                stack.remove(j)

    print in_degrees
    print connections

    finished = 0
    while stack:
        course = stack.pop(0)
        finished += 1
        for out_course in connections[course]:
            in_degrees[out_course] -= 1
            if in_degrees[out_course] == 0:
                stack.append(out_course)

    return finished == numCourses


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
    for courses in nexts:
        for course in courses:
            require_nums[course] += 1
            if course in stack:
                stack.remove(course)
    ans = []
    while stack:
        cur = stack.pop()
        ans.append(cur)
        for next in nexts[cur]:
            require_nums[next] -= 1
            if require_nums[next] == 0:
                stack.append(next)

    if len(ans) == numCourses:
        return ans
    else:
        return []

test =[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
print findOrder(10, test)