class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edge=[[] for i in range(numCourses)]
        ind=[0 for i in range(numCourses)]
        for info in prerequisites:
            edge[info[0]].append(info[1])
            ind[info[1]]+=1

        #从边缘列表转化成邻接矩阵
        que=collections.deque()
        flag=1
        while flag == 1:
            flag=0
            for index,j in enumerate(ind):
                if j==0:
                    que.append(index)
                    for ii in edge[index]:
                        ind[ii]-=1
                    flag=1
                    ind[index]=-1
        if len(que)==numCourses:
            return True
        else:
            return False
