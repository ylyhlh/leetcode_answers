# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=(x>0)-(x<0) # cmp(x,0) for python 2
        r=int(str(s*x)[::-1])
        return(r<2**31)*s*r