# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0 for i in range(len(num1) + len(num2))]
        
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i+j] += int(n1) * int(n2)
                res[i+j+1] += res[i+j]/10
                res[i+j] %= 10
        
        res_str = ''
        first_non_zero = False
        for i, v in enumerate(reversed(res)):
            if v != 0: 
                first_non_zero = True
            elif not first_non_zero:
                continue
            res_str += str(v)
        res_str = '0' if len(res_str) == 0 else res_str
        return res_str


class classname(object):
    pass



class Solution_0(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0 for i in range(len(num1) + len(num2))]
        
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i+j] += int(n1) * int(n2)
                res[i+j+1] += res[i+j]/10
                res[i+j] %= 10
        
        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join( map(str,res[::-1]) )