
def findMaxForm(strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """

    zeros = [0] * (len(strs)+1)
    ones = [0] * (len(strs)+1)

    for i, s in enumerate(strs):
        zeros[i+1] = s.count("0")
        ones[i+1] = s.count("1")
    dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs)+1)]  # dp[strs+1][m][n]

    for k in range(len(strs)+1):  # k 代表 前k个str
        for mm in range(m+1):  # mm 代表 0
            for nn in range(n+1):  # nn 代表1
                if k == 0 or (mm == 0 and nn == 0):
                    dp[k][mm][nn] = 0
                else:
                    if mm >= zeros[k] and nn >= ones[k]:
                        dp[k][mm][nn] = max(dp[k - 1][mm][nn], 1 + dp[k - 1][mm - zeros[k]][nn - ones[k]])
                    else:
                        dp[k][mm][nn] = dp[k - 1][mm][nn]

    return dp[len(strs)][m][n]

s=["10","0001","111001","1","0"]
print (findMaxForm(s,5,3))