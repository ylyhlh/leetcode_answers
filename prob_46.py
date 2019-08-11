# 46. Permutations
# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        res = []
        def generate(cans, hist):
            if len(hist) == N:
                res.append(hist)
                return
            for k in cans:
                generate([i for i in cans if i!=k], hist+[k])
        generate(nums, [])
        return res