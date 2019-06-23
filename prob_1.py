# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# solution 1: this needs to be careful of duplicate use of same number
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {k:i for i, k in enumerate(nums)}
        for i, k in enumerate(nums):
            res = target - k
            if res in nums_dict and nums_dict[res] != i:
                return i, nums_dict[res]
        return None
            
        