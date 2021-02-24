class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        f = [0 for i in range(n + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    f[j] = f[j] + 1
                else:
                    f[j] = 0
            stack = [-1]

            for k, num in enumerate(f):
                while f[stack[-1]] > num:
                    index = stack.pop()
                    res = max(res, f[index] * (k - stack[-1] - 1))
                stack.append(k)

        return res


s=Solution()
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))