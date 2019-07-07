# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        res = 0
        pivotal = 1
        for di in range(len(s)-1, -1, -1):
            cur = digit_map[s[di]]
            if cur >= pivotal:
                res += cur
                pivotal = cur
            else:
                res -= cur
        return res