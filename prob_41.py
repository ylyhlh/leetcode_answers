# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 0:
            return 1
        if 1 not in nums:
            return 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i]  = 1


        for i in range(n):
            nums[nums[i]%(n+1)-1]+= (n+1)
        for i in range(len(nums)):
            if nums[i] <= (n+1):
                return i+1
        return n +1