# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        cur = []
        nex = []
        if root == None:
            return ret
        flag = 1
        cur.append(root)

        while len(nex) != 0 or len(cur) != 0:
            ret.append([])
            while len(cur) != 0:
                ptr = cur.pop()
                ret[-1].append(ptr.val)
                if flag == 1:
                    if ptr.left != None:
                        nex.append(ptr.left)
                    if ptr.right != None:
                        nex.append(ptr.right)
                else:
                    if ptr.right != None:
                        nex.append(ptr.right)
                    if ptr.left != None:
                        nex.append(ptr.left)
            flag = flag * -1
            cur, nex = nex, cur
        return ret





