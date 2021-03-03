class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 :
            return
        self.presum=[[0 for j in range(len(matrix[0])+1)]for i in range(len(matrix)+1)]
        for i in range(0,len(matrix)+1):
            for j in range(0,len(matrix[0])+1):
                if i == 0 or j == 0:
                    self.presum[i][j]=0
                else:
                    self.presum[i][j] = matrix[i-1][j-1] + self.presum[i-1][j] + self.presum[i][j-1] - self.presum[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = self.presum[row2+1][col2+1] - self.presum[row2+1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]
        return res