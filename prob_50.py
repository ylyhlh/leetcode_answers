# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow(x, n):
            if n == 0:
                return 1
            half = pow(x, n//2)
            if n%2==0:
                return half*half
            else:
                return half*half*x
        if n>=0:
            return pow(x,n)
        else:
            return pow(1.0/x,-n)