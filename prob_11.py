# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        cur_max = 0
        
        while l < r:
            left_bigger = height[l] > height[r]
            cur_height = height[r] if left_bigger else height[l]
            cur_area = (r-l) * cur_height
            cur_max = cur_area if cur_area > cur_max else cur_max
            if left_bigger:
                r -= 1
            else:
                l += 1
        return cur_max