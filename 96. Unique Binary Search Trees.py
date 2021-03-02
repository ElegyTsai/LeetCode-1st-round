class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n + 2)] for j in range(n + 2)]

        for l in range(0, n + 2):
            for k in range(n + 2 - l):
                if l == 0 or l == 1 or l == 2:
                    dp[k][k + l] = 1
                else:
                    for ll in range(1, l):
                        dp[k][k + l] += dp[k][k + ll] * dp[k + ll][k + l]

        return dp[0][n + 1]

s=Solution()
print(s.numTrees(3))