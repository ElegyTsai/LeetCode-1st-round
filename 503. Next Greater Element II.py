class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[-1 for i in range(len(nums))]

        stack=[]
        stack.append(0)
        if len(nums) == 0 or len(nums)==1 :
            return res
        ii = 1
        i = ii % len(nums)
        while ii< 2*len(nums) :

            while  len(stack) != 0 and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]

            stack.append(i)
            ii = (ii + 1)
            i = ii %len(nums)


        return res
