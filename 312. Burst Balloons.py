class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.insert(0, 1)
        nums.append(1)

        dp = [[0 for i in range(0, l + 2)] for i in range(l + 2)]

        for ll in range(1, l + 2):
            for k in range(0, l + 2 - ll):
                if ll == 1:
                    dp[k][k + ll] = 0
                elif ll == 2:
                    dp[k][k + ll] = nums[k] * nums[k + 1] * nums[k + 2]
                else:
                    m = 0
                    for lll in range(1, ll):
                        m = max(dp[k][k + lll] + dp[k+lll][k + ll] + (nums[k] * nums[k + lll] * nums[k + ll]), m)
                    dp[k][k+ll]=m

        return dp[0][l + 1]
s=Solution()
print(s.maxCoins([3,1,5,8]))