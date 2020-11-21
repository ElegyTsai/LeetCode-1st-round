def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """

    def find(matrix, memo, row, col, r, c):

        deltar = [1, -1, 0, 0]
        deltac = [0, 0, -1, 1]
        res = [1]
        flag = 0

        for i in range(0, 4):
            if c + deltac[i] >= 0 and c + deltac[i] < col and r + deltar[i] >= 0 and r + deltar[i] < row:  # 边界条件
                if matrix[r + deltar[i]][c + deltac[i]] > matrix[r][c]:  # 大小条件

                    res.append(1 + find(matrix, memo, row, col, r + deltar[i], c + deltac[i]))

            memo[r][c] = max(res)
            return memo[r][c]

    row = len(matrix)
    col = len(matrix[1])

    memo = [[-1] * col for i in range(row)]

    r, c = 0, 0

    maxl = [0, 0]

    while r < row:
        c = 0
        while c < col:
            if memo[r][c] == -1:
                find(matrix, memo, row, col, r, c)

            if memo[maxl[0]][maxl[1]] < memo[r][c]:
                maxl = [r, c]

            c += 1
        r += 1
    # 结束遍历

    # 重新输出递增路径

    x, y = maxl
    ret = [matrix[x][y]]

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    while memo[x][y] != 1:
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if nx >= 0 and ny < col and ny >= 0 and nx < row:  # 边界条件
                if memo[x][y] - 1 == memo[nx][ny]:
                    x = nx
                    y = ny
                    ret.append(matrix[nx][ny])

    ret.reverse()
    return ret

m=[[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]

res=longestIncreasingPath(m)

for i in res:
    print(i)