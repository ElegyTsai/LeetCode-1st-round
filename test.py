class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum = 0
        stack = []
        for i in range(len(height)):
            while len(stack) != 0 and height[stack[-1]] < height[i]:
                idx = stack.pop()
                if len(stack)==0:
                    break
                sum += (min(height[stack[-1]],height[i]) - height[idx]) * (i - stack[-1] -1 )
            stack.append(i)

        return sum
s=Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))