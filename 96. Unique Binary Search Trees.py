
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]

        for l in range(n+1):
            if l == 0 or l == 1:
                dp[l] = 1
            else:
                for kk in range(0, l):
                    dp[l] += dp[kk] * dp[l - kk - 1]

        return dp[l]
s=Solution()
print(s.numTrees(3))