class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dic = {}
        for idx, tar in enumerate(t):
            if dic.get(tar) == None:
                dic[tar] = [idx]
            else:
                dic[tar].append(idx)

        dp = [0 for _ in range(len(t) + 1)]
        dp[0] = 1
        for ch in s:
            if dic.get(ch) != None:
                for i in range(len(dic[ch])-1,-1,-1):
                    loc = dic[ch][i]
                    dp[loc + 1] += dp[loc]
        return dp[-1]
s=Solution()
print(s.numDistinct("rabbbit","rabbit"))