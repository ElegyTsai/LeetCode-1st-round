class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1 = list(word1)
        word2 = list(word2)
        f = [[[] for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        # f[i][j] i->word1  j->word2

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 and j != 0:
                    f[i][j] = j - i
                elif i != 0 and j == 0:
                    f[i][j] = i - j

                else:
                    if word1[i - 1] == word2[j - 1]:
                        f[i][j] = min(f[i][j - 1] + 1, f[i - 1][j] + 1, f[i - 1][j - 1])
                    else:
                        f[i][j] = min(f[i][j - 1] + 1, f[i - 1][j] + 1, f[i - 1][j - 1] + 1)

        return f[-1][-1]