# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        
        l, r = 0, N-1
        while l+1 < r:
            m = (l+r)/2
            v =  nums[m]
            if target == v:
                return m
            if target < v:
                r = m
            else:
                l = m
        if nums[r] < target:
            return r + 1
        if nums[l] >= target:
            return l
        return r
        