class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[ for i in range(len(nums))]

        stack=[]
        stack.append(0)
        i=1 % len(nums)
        while len(stack) != 0 and i != stack[0]:

            while  len(stack) != 0 and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]
            if len(stack)!= 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
            i = (i + 1) % len(nums)

        return res

s=Solution()
print(s.nextGreaterElements([1,2,1]))