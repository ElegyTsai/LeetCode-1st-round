class Solution:
    def partition(self, s) :

        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        s = list(s)
        for i in range(0, len(s)):
            for k in range(0, len(s) - i):
                if i == 0:
                    dp[k][i + k] = 1
                elif i == 1:
                    if s[k] == s[k + 1]:
                        dp[k][k + i] = 1
                    else:
                        dp[k][k + i] = -1
                else:
                    if s[k] == s[k + i] and dp[k + 1][k + i - 1] == 1:
                        dp[k][k + i] = 1
                    else:
                        dp[k][k + i] = -1

        stack = []
        res = []

        def find(dp, stack, s, res, sta):
            i = sta
            while i < len(s) - 1:
                if dp[sta][i] == 1:
                    stack.append(i)
                    find(dp, stack, s, res, i+1)
                    i += 1
                else:
                    i += 1

            if dp[sta][i] == 1:
                # add
                res.append([])

                beg = 0
                stack.append(i)
                for split in stack:
                    res[-1].append("".join(s[beg:split + 1]))
                    beg = split + 1
                stack.pop()

            if stack:
                stack.pop()
            return

        find(dp, stack, s, res, 0)
        return res


s=Solution()
print(s.partition("aab"))