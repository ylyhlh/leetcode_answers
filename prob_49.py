# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for w in strs:
            s = tuple(sorted(w))
            if s not in ans:
                ans[s] = []
            ans[s].append(w)
        return ans.values()