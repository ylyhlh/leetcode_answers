# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/



class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if nums == [] or not nums:
            return [[]]
        
    
        nums = sorted(nums)
        
        result = []
        res = nums[:]
        self.helper(nums, res, [], result)
        
        return result
        
    def helper(self, nums, res, tmp_list, result):
        if len(tmp_list) == len(nums):
            result.append(tmp_list[:])
            
        for index in range(0, len(res)):
            
            if index > 0 and res[index] == res[index-1]:
                continue
                
            tmp_list.append(res[index])
            tmp_res = res[:]
            tmp_res.pop(index)
            self.helper(nums, tmp_res, tmp_list, result)
            tmp_list.pop()