class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [[[] for loc in range(n+1)] for i in range(n + 1)]

        for l in range(0, n + 1):
            for loc in range(n-l+1):
                if l == 0:
                    dp[l][loc].append(None)
                elif l == 1:
                    now = TreeNode()
                    now.val = loc + 1
                    dp[l][loc].append(now)

                else:
                    for kk in range(0, l ):
                        for leftnode in dp[kk][loc]:
                            for rightnode in dp[l - kk - 1][loc + kk +1]:
                                now = TreeNode()
                                now.val = loc + kk + 2
                                now.left = leftnode
                                now.right = rightnode
                                dp[l][loc].append(now)

        return dp[n][0]
s=Solution()
print(s.generateTrees(5))
