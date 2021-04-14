class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        height = n // digit / 10
        cur = n / digit % 10
        low = n % digit
        res = 0

        while height != 0 or cur != 0:

            if cur == 0:
                res += height * digit
            elif cur == 1:
                res += height * digit + low + 1
            else:
                res += (height + 1) * digit
            low += digit * cur
            cur = height % 10
            height = height // 10
            digit *= 10

        return res