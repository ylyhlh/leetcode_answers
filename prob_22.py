# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def add_next_char(pre, n_left, n_right):
            if len(pre) == 2*n:
                res.append(pre)
                return
            if n_left < n:
                add_next_char(pre+'(', n_left+1, n_right)
            if n_left > n_right:
                add_next_char(pre+')', n_left, n_right+1)
        add_next_char('', 0, 0)
        return res