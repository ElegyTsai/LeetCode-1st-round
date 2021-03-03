class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """

        store = [0 for i in range(50000)]
        now = 0
        res = 0
        last = 0

        def find(store, now, last):
            while now <= last and store[now] == 0:
                now += 1
            if now > last:
                return -1
            elif now <= last:
                return now

        while now < len(days) or now<=last:
            if now < len(days):
                badday = now + days[now]-1

                store[badday] += apples[now]
                if badday > last:
                    last = badday
                eat=find(store, now, last)
                if eat != -1:
                    store[eat] -= 1
                    res += 1
                now += 1
            else:
                eat=find(store, now, last)
                res += min(store[eat],eat-now+1)
                now =eat+1


        return res
s=Solution()
print(s.eatenApples([1],[2]))