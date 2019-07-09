# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        
        imin, imax, half_len = 0, m, (m + n + 1) / 2 # this is actually faster than do it separately
        
        while imin <= imax:
            i = (imin + imax) /2
            j = half_len - i
            if i>0 and A[i-1] > B[j]:
                imax = i - 1
            elif i<m and A[i] < B[j-1]:
                imin = i + 1
            else:
                if i == 0: 
                    left_max = B[j-1]
                elif j == 0: 
                    left_max = A[i-1]
                else:
                    left_max = max(A[i-1], B[j-1])
                if (m + n) % 2 == 1:
                    return left_max
                if i == m: 
                    right_min = B[j]
                elif j == n: 
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                return (right_min + left_max) /2.0
