class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        l = len(A) - 1
        flag = 0
        while K != 0 or flag != 0:
            if l == -1:
                i = flag + (K % 10)
            else:
                i = A[l] + flag + (K % 10)
            if l == -1:
                A.insert(0, i % 10)
                K=K//10
            else:
                A[l] = i % 10
                l -= 1
                K = K // 10
            if i >= 10:
                flag = 1
            else:
                flag = 0

        return A


s=Solution()
A=[1]
K=9999

res=s.addToArrayForm(A,K)
print(res)