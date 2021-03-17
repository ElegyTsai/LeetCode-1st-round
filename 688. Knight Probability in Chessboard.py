class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) :
        if K == 0 and r < N and c < N:
            return 1
        global mv
        mv = [[-1, 2], [-1, -2], [-2, 1], [-2, -1], [1, 2], [1, -2], [2, 1], [2, -1]]

        dp = [[[0 for i in range(K - 1)] for j in range(N)] for k in range(N)]
        # dp[i][j][step]

        for step in range(0, K - 1):
            for i in range(N):
                for j in range(N):
                    if step == 0:
                        out = 0
                        for m in mv:
                            nr = i + m[0]
                            nc = j + m[1]
                            if nr >= N or nr < 0 or nc >= N or nc < 0:
                                out += 1
                        dp[i][j][step] = (8.0 - out) / 8
                    else:
                        for m in mv:
                            nr = i + m[0]
                            nc = j + m[1]
                            if nr >= N or nr < 0 or nc >= N or nc < 0:
                                continue
                            else:
                                dp[i][j][step] += dp[nr][nc][step - 1] / 8.0

        ret = 0
        for m in mv:
            nr = r + m[0]
            nc = c + m[1]
            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue
            else:
                if K == 1:
                    ret += 1 / 8.0
                else:
                    ret += dp[nr][nc][K - 2] / 8.0

        return ret

s=Solution()
print(s.knightProbability(10,13,5,3))