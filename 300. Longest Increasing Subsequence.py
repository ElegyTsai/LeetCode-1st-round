class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            m=0
            for j in range(0,i):
                if dp[j]>m and nums[j]<nums[i]:
                    m=dp[j]
            dp[i]=m+1
        m = 1
        for j in range(len(nums)):
            if dp[j] > m :
                m = dp[j]


        return m




r=Solution()
print(r.lengthOfLIS([10,9,2,5,3,7,101,18]))
