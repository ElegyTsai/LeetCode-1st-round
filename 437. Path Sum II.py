# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        v=dict()
        v[0] = 1
        res = 0
        if root == None:
            return 0
        def pretravel(root: TreeNode,presum:int) -> int:
            nonlocal res,v,sum
            cur =  root.val + presum
            if v.get(cur-sum) != None and v.get(cur-sum) != 0:
                res += v.get(cur-sum)
            if v.get(cur) != None:
                v[cur] += 1
            else:
                v[cur] = 1
            if root.left != None:
                pretravel(root.left,cur)
            if root.right !=None:
                pretravel(root.right,cur)
            v[cur] -= 1
        pretravel(root,0)
        return res
