# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ## Edge Cases
        len_hay = len(haystack)
        len_needle = len(needle)
        diff = len_hay - len_needle
        
        if diff < 0:
            return -1
        if diff == len_hay:
            return 0
        for i in range(0, diff + 1): 
            # if haystack[i] == needle[0]:
            if haystack[i:i + len_needle] == needle:
                return i
            
        return -1