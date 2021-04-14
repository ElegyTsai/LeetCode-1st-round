class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])

        def find(target, left, right):
            if matrix[left / n][left % n] == target or matrix[right / n][right % n] == target:
                return True
            elif right - left == 1:
                return False

            mid = (left + right) / 2
            if matrix[mid / n][mid % n] > target:
                if matrix[left / n][left % n] > target:
                    return False
                else:
                    return find(target, left, mid)
            else:
                if matrix[right / n][right % n] < target:
                    return False
                else:
                    return find(target, mid, right)

        return find(target, 0, m * n - 1)
