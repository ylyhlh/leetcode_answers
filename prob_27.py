# 27. Remove Element
# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write_p = 0
        for _, num in enumerate(nums):
            if num != val:
                nums[write_p] = num
                write_p += 1
        
        return write_p

