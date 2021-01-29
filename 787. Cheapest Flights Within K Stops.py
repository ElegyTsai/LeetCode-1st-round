import collections
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        log=[0 for i in range(n)]
        adj = [[] for i in range(n)]
        for edge in flights:
            adj[edge[0]].append([edge[1], edge[2]])

        price = [[-1 for i in range(K+2)] for i in range(n)]
        price[src][0]=0

        def Travel(log,now, i, price):
            for n in range(len(price[now]) - 1):
                cost = price[now][n]
                if cost != -1:
                    if price[i[0]][n + 1] > cost + i[1] or price[i[0]][n + 1]==-1:
                        price[i[0]][n + 1] = cost + i[1]
                        log[i[0]]=-1
            return

        que = collections.deque()
        que.append(src)
        while len(que) != 0:
            now = que.pop()
            if log[now]==1:
                continue
            log[now]=1
            for i in adj[now]:
                Travel(log,now, i, price)
                que.appendleft(i[0])

        m = 0
        res = max(price[dst])
        while m <= K+1:
            if price[dst][m] <= res and price[dst][m] != -1:
                res = price[dst][m]
            m += 1

        return res

s=Solution()
#print(s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
print(s.findCheapestPrice(5,[[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]],0,4,3))
