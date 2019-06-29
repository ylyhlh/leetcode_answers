# 6. ZigZag Conversion
# https://leetcode.com/problems/zigzag-conversion/


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        # list of string to store string
        rows = ['' for i in range(numRows)]
        cur_row_i = 0
        direction = 1 # flip to -1 when touched to row 3, flop to 1 when touched to row 0
        for ch in s:
            rows[cur_row_i] = rows[cur_row_i] + ch
            if cur_row_i == 0:
                direction = 1
            if cur_row_i == numRows-1:
                direction = -1
            cur_row_i += direction
        return ''.join(rows)