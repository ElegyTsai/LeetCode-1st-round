class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        prefix=[0 for i in A]
        s=0
        for i in range(len(A)):
            s += A[i]
            prefix[i] =s

        def getsum(i,j,prefix):
            if i>j:
                return 0
            elif i==0:
                return prefix[j]
            else:
                return prefix[j]-prefix[i-1]

        ret = getsum(0,M+L-1,prefix)
        for ll in range(L + M + 1, len(A)+1):
            for blank in range(0 , ll-M-L + 1):
                ret = max(ret, getsum(ll - M - L - blank, ll - 1, prefix) - getsum(ll - M  - blank, ll - 1 - M  , prefix))
                ret = max(ret, getsum(ll - M - L - blank, ll - 1, prefix) - getsum(ll - L  - blank, ll - 1 - L  , prefix))


        return ret
s=Solution()