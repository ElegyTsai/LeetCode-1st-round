class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=nums[0]
        cont=nums[0]
        for i in range(1,len(nums)):
            cont=max(cont+nums[i],nums[i])
            maxi=max(maxi,cont)
        return maxi

