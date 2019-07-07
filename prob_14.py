# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_str = min(strs, key=len)
        
        for i, char in enumerate(min_str):
            
            for other in strs:
                if other[i] != char:
                    return min_str[:i]
        
        return min_str
        