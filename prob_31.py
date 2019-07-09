# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N <= 1:
            return nums
        i = N - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i == -1: 
            l, r = 0, N-1
        else:
            j = i+1
            p = nums[i]
            while j < N and nums[j] > p:
                j += 1
            j -= 1
            nums[i] = nums[j]
            nums[j] = p
            l, r = i+1, N-1
        nums
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
