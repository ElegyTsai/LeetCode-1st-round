class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [[0 for n in range(len(S))] for _ in range(len(S))]
        for i in range(len(S)):
            for j in range(len(S) - i):
                if i == 0:
                    dp[j][j + i] = 1
                elif i == 1:
                    dp[j][j + i] = 2
                elif S[j] == S[j + i]:
                    l = 0
                    r = 0
                    for k in range(1, i):
                        if S[j + k] == S[j]:
                            l = k
                            break
                    for k in range(1, i):
                        if S[j + i - k] == S[j]:
                            r = i - k
                            break
                    if l == 0:
                        dp[j][j + i] = 2 * dp[j + 1][j + i - 1] + 2
                    elif l == r and l != 0:
                        dp[j][j + i] = 2 * dp[j + 1][j + i - 1] + 1
                    elif l != r and r-l>=2:
                        dp[j][j + i] = 2 * dp[j + 1][j + i - 1] - dp[j + l + 1][j + r - 1]
                    else:
                        dp[j][j + i] = 2 * dp[j + 1][j + i - 1]

                elif S[j] != S[j + i]:
                    dp[j][j + i] = dp[j][j + i - 1] + dp[j + 1][j + i] - dp[j + 1][j + i - 1]

        return dp[0][len(S) - 1]%100000007

S=Solution()
print(S.countPalindromicSubsequences('aaaa'))