import collections
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: intimport collections
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for l in range(len(s)):
            for k in range(0,len(s)-l):
                if l == 0:
                    dp[k][k+l] = True
                elif l == 1:
                    dp[k][k+l] = (s[k] == s[k+l])
                else:
                    dp[k][k+l] = (s[k] == s[k+l]) and dp[k+1][k+l-1]
        res=0
        stack=collections.deque([0])
        log=dict()
        for i in range(len(s)):
            log[i]=0

        while stack:
            sl = len(stack)
            for i in range(sl):
                sta= stack.pop()
                i  = sta
                while i<len(s)-1:
                    if dp[sta][i]:
                        if log[i] == 0 or res == 0:
                            stack.appendleft(i+1)
                            log[i] = 1
                    i +=1
                if dp[sta][i] == True:
                    return res
            res += 1
        return 1


s=Solution()
print(s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))
        """
        s = list(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for l in range(len(s)):
            for k in range(0,len(s)-l):
                if l == 0:
                    dp[k][k+l] = True
                elif l == 1:
                    dp[k][k+l] = (s[k] == s[k+l])
                else:
                    dp[k][k+l] = (s[k] == s[k+l]) and dp[k+1][k+l-1]
        res=0
        stack=collections.deque([0])
        log=dict()
        for i in range(len(s)):
            log[i]=0

        while stack:
            sl = len(stack)
            for i in range(sl):
                sta= stack.pop()
                i  = sta
                while i<len(s)-1:
                    if dp[sta][i]:
                        if log[i] == 0 or res == 0:
                            stack.appendleft(i+1)
                            log[i] = 1
                    i +=1
                if dp[sta][i] == True:
                    return res
            res += 1
        return 1


s=Solution()
print(s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))