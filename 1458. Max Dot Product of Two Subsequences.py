class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        # m->nums1 n->nums2   DP[m][n] index count from 1

        for n in range(len(nums2) + 1):
            if n == 0:
                for mm in range(len(nums1) + 1):
                    dp[mm][n] = -1000000
            else:
                opt = -1000000
                for m in range(len(nums1) + 1):
                    if m == 0:
                        dp[m][n] = -1000000
                        continue

                    dp[m][n]=max(dp[m - 1][n - 1] + nums1[m - 1] * nums2[n - 1],nums1[m - 1] * nums2[n - 1],dp[m - 1][n],dp[m][n - 1])





        return dp[len(nums1)][len(nums2)]

s=Solution()
print(s.maxDotProduct([-5,-1,-2],[3,3,5,5]))