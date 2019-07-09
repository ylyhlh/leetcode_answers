# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)
        def find_left():
            l, r = 0, N-1
            while l<r:
                p = (l+r)/2
                if nums[p] == target:
                    r = p
                elif nums[p] < target:
                    l = p + 1
                else:
                    r = p - 1
            return l
        def find_right():
            l, r = 0, N -1
            while l<r:
                p = (l+r)//2
                if nums[p] <= target:
                    l = p + 1
                else:
                    r = p
            # this is important !!!
            if l < N and nums[l] == target:
                return l
            return l - 1
        if N==1:
            return (-1,-1) if nums[0] != target else (0,0)
        left = find_left()
        if left == N or nums[left] != target:
            return [-1,-1]
        return [left, find_right()]

#other's solution
class Solution_1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                res.append(mid)
                break
            elif target < nums[mid] or target == nums[mid] and nums[mid-1] == target:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid+1] > target):
                res.append(mid)
                return res
            elif target > nums[mid] or target == nums[mid] and nums[mid+1] == target:
                left = mid + 1
            else:
                right = mid - 1

        return res 