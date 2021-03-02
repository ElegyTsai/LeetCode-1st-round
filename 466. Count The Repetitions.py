class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        def search(cur,loc,dp,s1,s2,k1,k2,m):
            if dp[cur][loc] == -2:
                dp[cur][loc]  =[m,k1,k2]
                return  1,s1.find(s2[cur],loc),[m,k1,k2]
            else:
                ret = [m-dp[cur][loc][0],k1-dp[cur][loc][1],k2-dp[cur][loc][2]]
                dp[cur][loc] = [m,k1,k2]

                return -1,s1.find(s2[cur],loc),ret

        ls1=list(s1)
        ls2=list(s2)
        dp=[[-2 for j in range(len(s1))] for i in range(len(s2))]
        m=0
        cur=0
        k2=0
        k1=0
        loc=0
        while  k1 < n1:

            res,locn,delta = search(cur,loc,dp,s1,s2,k1,k2,m)

            if res==-1 and n1-k1 > delta[1]:

                rep= (n1 - k1 - 1) // delta[1]
                k2 += delta[2] * rep
                k1 += delta[1] * rep
                m  += delta[0] * rep + (k2 // n2)
                k2 = k2 % n2
                loc = locn + 1

            elif  locn == -1:
                res,locn,delta = search(cur,0,dp,s1,s2,k1,k2,m)
                loc=locn+1
                k1 += 1
                if locn == -1 :
                    return 0

            else:
                loc=locn+1


            cur += 1
            if cur == len(s2) :
                cur = 0
                k2 += 1
                if k2 == n2:
                    k2 = 0
                    m += 1
            if loc == len(s1):
                loc = 0
                k1 += 1
        return m

s=Solution()
print(s.getMaxRepetitions("nlhqgllunmelayl",10000,"lnl",10))
print(s.getMaxRepetitions("acb",4,"ab",2))