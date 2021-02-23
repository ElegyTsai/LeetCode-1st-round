class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[[] for i in range(len(s))] for j in range(len(s))]
        s = list(s)
        ret = [0, 0]
        for i in range(1, len(s)):
            for k in range(len(s) - i):
                if i == 1 or i == 2:
                    if s[k] == s[k + i]:
                        if i > ret[1]:
                            ret = [k, i]
                        dp[k][k + i] = True
                else:
                    if s[k] == s[k + i]:
                        if dp[k + 1][k + i - 1] == True:

                            if i > ret[1]:
                                ret = [k, i]
                            dp[k][k + i] = True

                    else:
                        dp[k][k + i] = False
        s = "".join(s)
        res = "".join(s[ret[0]:ret[0] + ret[1] + 1])

        return res