# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        lmax = rmax = 0
        ans = 0
        while l<r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
                l+=1
            else:
                rmax = max(rmax, height[r])
                ans += rmax - height[r]
                r-=1
        return ans

class Solution_0(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = [ 0 for i in height]
        right = [ 0 for i in height]
        max_cur = 0
        for k, v in enumerate(height):
            max_cur = max(max_cur, v)
            left[k] = max_cur
        max_cur = 0
        for k in range(len(height)-1,-1, -1):
            max_cur = max(max_cur, height[k])
            right[k] = min(max_cur, left[k]) - height[k]
        return sum(right)