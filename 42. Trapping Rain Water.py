class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        s = 0
        for i, h in enumerate(height):
            while len(stack) != 0 and height[stack[-1]] < h:

                bot = stack.pop()
                if len(stack) == 0:
                    break
                else:
                    s += (min(h, height[stack[-1]]) - height[bot]) * (i - stack[-1] - 1)
            stack.append(i)
        return s
