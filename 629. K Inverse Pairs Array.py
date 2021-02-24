class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

        for nn in range(n+1):
            for kk in range(k+1):
                if nn==0 and kk!=0:
                    dp[nn][kk]=0
                    continue
                elif kk==0:
                    dp[nn][kk]=1
                else:
                    if kk>=nn:
                        dp[nn][kk]=dp[nn-1][kk]+dp[nn][kk-1]-dp[nn-1][kk-nn]
                    else:
                        dp[nn][kk]=dp[nn-1][kk]+dp[nn][kk-1]

        return dp[-1][-1] %1000000007

s=Solution()
print(s.kInversePairs(4,3))