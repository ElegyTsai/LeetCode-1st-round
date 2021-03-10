class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type k: int
        :rtype: int
        """

        def search(n, sta):
            k1 = n + 1
            while k1 < len(sta) and sta[k1] != 1:
                k1 += 1

            if k1 == len(sta):
                res1 = -1
            else:
                res1 = k1 - n
            k2 = n - 1
            while k2 >= 0 and sta[k2] != 1:
                k2 -= 1

            if k2 == -1:
                res2 = -1
            else:
                res2 = n - k2

            return res1, res2

        sta = [0 for i in range(len(bulbs))]
        for day, n in enumerate(bulbs):
            sta[n - 1] = 1
            k1, k2 = search(n - 1, sta)
            if k1 == k or k2 == k:
                return day

        return -1

s=Solution()
print(s.kEmptySlots())