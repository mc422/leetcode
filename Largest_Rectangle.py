class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stackHeight = []
        stackIndex = []
        for i in range(len(height)):
            if stackHeight == [] or height[i] > stackHeight[len(stackHeight)-1]:
                stackHeight.append(height[i]); stackIndex.append(i)
            elif height[i] < stackHeight[len(stackHeight)-1]:
                lastIndex = 0
                while stackHeight and height[i] < stackHeight[len(stackHeight)-1]:
                    lastIndex = stackIndex.pop()
                    tempArea = stackHeight.pop() * (i-lastIndex)
                    if maxArea < tempArea: maxArea = tempArea
                stackHeight.append(height[i]); stackIndex.append(lastIndex)
        while stackHeight:
            tempArea = stackHeight.pop() * (len(height) - stackIndex.pop())
            if tempArea > maxArea:
                maxArea = tempArea
        return maxArea

solution = Solution()
print solution.largestRectangleArea([1,3,5,7,4,2])