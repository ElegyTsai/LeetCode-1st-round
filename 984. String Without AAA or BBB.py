class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        flag = 1
        res = []
        while a != 0 and b != 0:
            if a > b:
                res.append("aab")
                a -= 2
                b -= 1
                flag = 1
            elif b > a:
                res.append("bba")
                a -= 1
                b -= 2
                flag = 2
            else:

                res.append("ab")
                a -= 1
                b -= 1
        if a != 0:
            for i in range(a):
                res.append("a")
        if b != 0:
            for i in range(b):
                res.append("b")

        return "".join(res)


