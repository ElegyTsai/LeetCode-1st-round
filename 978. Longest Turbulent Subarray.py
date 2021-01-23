class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        dp=[0 for i in range(len(arr))]
        dp[0]=1
        if len(arr)==2:
            if arr[0]!=arr[1]:
                return 2
            else:
                return 1
        elif len(arr)==1:
            return 1
        if arr[0] != arr[1]:
            dp[1]=2
        else:
            dp[1]=1
        for i in range(2,len(arr)):
            if (arr[i]-arr[i-1])*(arr[i-1]-arr[i-2])<0:
                dp[i]=dp[i-1]+1
            elif (arr[i]-arr[i-1])==0:
                dp[i]=1
            else:
                dp[i]=2
        return max(dp)

a=Solution()
print(a.maxTurbulenceSize([37,199,60,296,257,248,115,31,273,176]))