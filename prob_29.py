# 29. Divide Two Integers
# https://leetcode.com/submissions/detail/239804731/
class Solution:
    def divide(self, dividend, divisor):
        if dividend >= 0 and divisor >= 0 or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        
		# some shortcuts
        if divisor == -1 and dividend == -2147483648:
            return 2147483647
        elif divisor == 1:
            return abs(dividend) if sign == 1 else -abs(dividend)
        
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        if dividend < divisor:
            return 0

        d = divisor 
        q = 1
        res = 0
        rest = dividend
        
        while True:
            t = d << 1
            if rest >= t:
                q += q
                d = t
            else:
                res += q
                q=1
                rest -= d
                d = divisor
                if (d<<1) > rest:
                    if rest>= d:
                        res += 1
                    break

        return res if sign == 1 else -res