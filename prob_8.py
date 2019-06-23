# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

import re,sys
INT_MAX=2**31 - 1
INT_MIN=-2**31


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        regex = re.match(r" *([-+]?\d+)", str)
        if regex:
            regex_int = int(regex.group(1))
            if regex_int > INT_MAX:
                return INT_MAX
            if regex_int < INT_MIN:
                return INT_MIN
            return regex_int
        return 0