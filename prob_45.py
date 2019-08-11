# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        pre_max_reach = max_reach = 0
        
        for i in range(len(nums)-1): # IMPortant do not scan the last one
            max_reach = max(i+nums[i], max_reach)
            if i == pre_max_reach:
                jumps += 1
                pre_max_reach = max_reach
        return jumps