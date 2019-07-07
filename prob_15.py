# 15. 3Sum
# https://leetcode.com/problems/3sum/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.threeSum_withtarget(nums, 0)
        
    def threeSum_withtarget(self, nums, target):
        res = []
        N = len(nums)
        if N < 3: return res
        nums.sort()
        if nums[0] > target or nums[N-1] < target:
            return []
        if nums[0] == target and  nums[N-1] == target:
            return [[target, target, target]]
        
        for i in range(N-2): # j k for last
            new_target = target - nums[i]
            l, r = i+1, N-1
            if  i!=0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                cur_sum = nums[l] + nums[r]
                if cur_sum > new_target:
                    r -= 1 #move r
                elif cur_sum < new_target:
                    l += 1# move l
                else: # equal to target
                    res.append((nums[i], nums[l], nums[r]))
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
        return res