class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """

        def find(x):
            if f[x][0] != x:
                return find(f[x][0])
            else:
                return x

        def diccmp(str1, str2):
            l1 = list(str1)
            l2 = list(str2)
            i = 0
            while i < len(l1) or i < len(l2):
                if i == len(l1):
                    return str1, str2
                if i == len(l2):
                    return str2, str1
                ch1 = l1[i]
                ch2 = l2[i]
                if ch1 < ch2:
                    return str1, str2
                elif ch1 > ch2:
                    return str2, str1
                i = i + 1

        def merge(x, y):
            sml, lag = diccmp(x, y)
            if f.get(sml) != None and f.get(lag)!= None:
                f[lag][0] = find(sml)
                f[sml][1] = f[sml][1] + f[lag][1]

        f = {}
        for name in names:
            n, cnt = name.split("(")
            cnt = int("".join(list(cnt)[:-1]))
            f[n] = [n, cnt]
        res = []
        for syn in synonyms:
            name1, name2 = syn.split(",")
            name1 = "".join(list(name1)[1:])
            name2 = "".join(list(name2)[0:-1])
            merge(name1, name2)

        resname = []
        resfeq = []
        for fname in f:
            tmpname = find(fname)
            if resname.count(tmpname) == 0:
                resname.append(tmpname)
                resfeq.append(f[tmpname][1])

        for c, nn in zip(resname, resfeq):
            res.append(c + "(" + str(nn) + ")")
        return res



s=Solution()
print(s.trulyMostPopular(["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"],["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]))




