class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [0 for _ in range(len(S))]
        for i in range(len(S)):
            if i == 0:
                dp[i] = 1
                continue
            for j in range(0, i):
                if S[i - j - 1] == S[i]:
                    break

            if j == i-1 and S[0] != S[i]:
                dp[i] = 2 * dp[i - 1] + 1
            elif j != i-1:
                dp[i] = 2 * dp[i - 1] - dp[i - 2 - j]
            else:
                dp[i] = 2 * dp[i - 1]

        return dp[-1] % 100000007
s=Solution()
print(s.distinctSubseqII('aaa'))