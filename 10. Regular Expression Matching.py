class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(ci, cj):
            if cj == '.':
                return True
            elif cj == ci:
                return True
            else:
                return False

        f = [[[] for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        # f[i][j]  i->s j->p   count from 1
        f[0][0] = True
        for i in range(len(s) + 1):
            for j in range(len(p) + 1):
                if i == 0 and j == 0:
                    f[i][j] = True


                elif i!=0 and j==0:
                    f[i][j]=False
                elif i==0 and j!=0:
                    if p[j-1]!='*':
                        f[i][j]=False
                    else:
                        f[i][j]=f[i][j-2]

                elif p[j - 1] == '*':
                    if match(s[i - 1], p[j - 2]):
                        f[i][j] = f[i - 1][j] or f[i][j - 2]
                    else:
                        f[i][j] = f[i][j - 2]
                else:
                    if match(s[i - 1], p[j - 1]):
                        f[i][j] = f[i - 1][j - 1]
                    else:
                        f[i][j] = False

        return f[len(s)][len(p)]

s=Solution()
print(s.isMatch("a","aa"))