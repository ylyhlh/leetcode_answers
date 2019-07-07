# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        write_idx = 1
        l = nums[0]
        for read_idx in range(1, len(nums)):
            r = nums[read_idx]
            if r != l:
                l = nums[write_idx] = r
                write_idx += 1
        return write_idx
