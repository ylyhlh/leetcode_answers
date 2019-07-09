# 38. Count and Say
# https://leetcode.com/problems/count-and-say/


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        res = '1'
        while i<n:
            new_res = ''
            count = 1
            for j in range(1, len(res)):
                if res[j-1] != res[j]:
                    new_res += str(count) + res[j-1]
                    count = 1
                else:
                    count += 1
            new_res += str(count) + res[-1]
            res = new_res
            i += 1
        return res