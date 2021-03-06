class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [-1 for i in range(num + 1)]
        if num == 0:
            return [0]
        res[0] = 0
        res[1] = 1
        for i in range(len(res)):
            if i == 0 or i == 1:
                continue
            else:
                res[i] = res[i // 2] + i % 2

        return resd

