class UnionFind(object):
    def __init__(self, equations,values):
        self.var = {}
        for alp,val in zip(equations,values):
            if self.var.find(alp[0])==None and self.var.find(alp[1]) ==None:
                self.var[alp[0]]=[1,alp[0]]
                self.var[alp[1]]=[val,alp[0]]

            self.var[name] = name

    def union(self, a, b):
        if a not in self.parent or b not in self.parent:
            return
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a < root_b:
            self.parent[root_b] = root_a
        else:
            self.parent[root_a] = root_b

    def find_root(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """



