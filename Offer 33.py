class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """

        def findtree(left,right):
            if left>= right :
                return True
            root=postorder[right]
            flag=-10
            for i in range(left,right):
                if flag==-10:
                    if postorder[i]<root:
                        continue
                    else:
                        flag=i-1
                else:
                    if postorder[i]<root:
                        return False
            if flag==-10:
                return findtree(left,right-1)
            else:
                return findtree(left,flag) and findtree(flag+1,right-1)

        n=len(postorder)-1
        return findtree(0,n)

