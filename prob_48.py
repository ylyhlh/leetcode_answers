# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix) == 0:
            return matrix
        N = len(matrix)
        for i in range(N//2):
            for j in range(i,N-i-1): 
                matrix[i][j], matrix[N-1-j][i], matrix[N-1-i][N-1-j],matrix[j][N-1-i]  =matrix[N-1-j][i], matrix[N-1-i][N-1-j], matrix[j][N-1-i] , matrix[i][j]
                 
