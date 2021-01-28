class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Pre=[0 for i in range(len(nums)+2)]
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            return 0
        for i in range(1,len(nums)+1):
            Pre[i]=Pre[i-1]+nums[i-1]
        Pre[-1]=Pre[-2]
        s=Pre[-1]
        for i in range(1,1+len(nums)):
            if Pre[i-1]==s-Pre[i]:
                return i-1
        return -1

s=Solution()
print(s.pivotIndex([1,7,3,6,5,6]))