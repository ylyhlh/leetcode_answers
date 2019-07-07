# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return None

        nums.sort()
        N = len(nums)
        res = []
        for k in range(N - 2):
            cur_target = target - nums[k]
            l = k + 1
            r = N - 1
            while l<r:
                # this is super important to skip unneeded loop!!!!!!!!!!!!!!!!
                if nums[k] + nums[r] + nums[r - 1] < target:
                    res.append(nums[k] + nums[r] + nums[r - 1])
                    break
                if nums[l] + nums[k] + nums[l + 1] > target:
                    res.append(nums[l] + nums[k] + nums[l + 1])
                    break
                cur_v = nums[l] + nums[r]
                res.append(cur_v + nums[k])
                if cur_v < cur_target:
                    l += 1
                if cur_v > cur_target:
                    r -= 1
                if cur_v == cur_target:
                    return target
        res.sort(key = lambda x: abs(x- target))
        return res[0]