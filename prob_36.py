# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = [{} for i in range(9)]
        rows = [{} for i in range(9)]
        boxs = [{} for i in range(9)]
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v != '.':
                    if v in cols[j]:
                        return False
                    cols[j][v] = 1
                    if v in rows[i]:
                        return False
                    rows[i][v] = 1
                    box_index = (i // 3 ) * 3 + j // 3
                    if v in boxs[box_index]:
                        return False
                    boxs[box_index][v] = 1
        return True
    