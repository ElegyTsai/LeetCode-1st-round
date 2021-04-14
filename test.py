"""
2 4 7 3
2 15 1
6 11 1
8 6 1
1 10 3
3 5 5
8 17 5
8 12 5
"""
a = [int(i) for i in input().split()]
v = a[0]
x0 = a[1]
n = a[2]
m = a[3]
fruit = [[0,0,0]]
for _ in range(n):
    f = [int(i) for i in input().split()]
    f[0], f[1] = f[1], f[0]
    fruit.append(f)

fruit.sort()

dp = [{} for _ in range(n + 1)]
dp[0] = {0: [x0, 0]}
# dp = [ {miss:x0,score}] x0,score,miss
maxscore = 0
for i in range(1, n + 1):
    curx = fruit[i ][1]
    cury = fruit[i][0]
    w = fruit[i ][2]
    j = i - 1
    while j >= 0 and j - i < m:
        if not dp[j]:
            j-=1
            continue
        for miss in list(dp[j]):
            curmiss = i - j - 1 + miss
            if curmiss >= m:  # 游戏会结束
                break
            elif abs(dp[j][miss][0] - curx) <= v * (cury - fruit[j][0]):  # 能接到
                if not dp[i]:
                    dp[i][curmiss] = [curx, dp[j][miss][1] + w]
                    maxscore=max(maxscore,dp[j][miss][1] + w)
                else:
                    # 比较过程
                    if dp[i].get(curmiss) == None:
                        ccurmiss = curmiss

                        while dp[i].get(ccurmiss) == None and curmiss >= 0:
                            ccurmiss -= 1
                        if dp[i].get(ccurmiss) == None:
                            dp[i][curmiss] = [curx, dp[j][miss][1] + w]
                            maxscore = max(maxscore, dp[j][miss][1] + w)
                        else:
                            if dp[i].get(ccurmiss)[1] < dp[j][miss][1] + w:
                                dp[i][curmiss] = [curx, dp[j][miss][1] + w]
                                maxscore = max(maxscore, dp[j][miss][1] + w)
                    else:
                        if dp[i][curmiss][1] < dp[j][miss][1] + w:
                            dp[i][curmiss] = [curx, dp[j][miss][1] + w]
                            maxscore = max(maxscore, dp[j][miss][1] + w)
        j-=1
print(maxscore)