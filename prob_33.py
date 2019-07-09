# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        def find_rot_index():
            l, r = 0, N-1
            # avoid search if not break, and this will resolve the problem if short arry
            if nums[l] <= nums[r]:
                return 0
            while l <= r:
                p = (l+r)//2
                if nums[p] > nums[p+1]:
                    return p + 1
                elif nums[p] >= nums[l]:
                    l = p + 1
                else:
                    r = p - 1
            return l+1 # no need
        
        
        def binary_search(l, r):
            
            while l<=r:
                p = (l+r)//2
                if nums[p] == target:
                    return p
                elif nums[p] < target:
                    l = p + 1
                else:
                    r = p -1
            return -1
        if N == 0:
            return -1
        if N == 1:
            return 0 if nums[0] == target else -1 
        
        first_id = find_rot_index()
        if nums[first_id] == target:
            return first_id
        if first_id == 0:
            return binary_search(0, N-1)
        # if nums[first_id] > target: return -1
        if nums[0] > target: 
            return binary_search(first_id, N-1)
        else:
            return  binary_search(0, first_id-1)
            
        
   