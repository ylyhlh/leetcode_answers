# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Solution 1: this failed: Time Limit Exceeded
class Solution_0(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_i, max_j = 0,0
        max_len = 0
        def check_palindromic(_sub_str):
            for i in range(len(_sub_str)/2 + 1):
                if _sub_str[i] != _sub_str[len(_sub_str)-1-i]:
                    return False
            return True
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                cur_len = j-i
                if cur_len>max_len:
                    if check_palindromic(s[i:j]):
                        max_len = cur_len
                        max_i, max_j = i, j
        return s[max_i:max_j]


# Solution 2: 5.50%
class Solution_1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_i, max_j = 0,0
        n = len(s) # length of string
        import numpy as np
        valid_mat = np.zeros((n,n))
        # initiate know values
        for i in range(n):
            valid_mat[i,i] = 1
            # check length 2 required?
            if i != n-1: # not last row:
                if s[i] == s[i+1]:
                    valid_mat[i,i+1] = 1
                    max_i, max_j = i, i+1
        print(valid_mat)
        
        # loop over length to fill the upper right matrix
        for cur_len in range(2, n):
            for i in range(n):
                j = i + cur_len
                if j < n:
                    if valid_mat[i+1,j-1] == 1 and s[i] == s[j]:
                        valid_mat[i, j] = 1
                        max_i, max_j = i, j
        return s[max_i: max_j+1]
# Solution 3:  83.84% 

class Solution:
    def get_max_len(self, s: 'list', left: 'int', right: 'int') -> 'int':
        n = len(s)
        for cur_len in range(n):
            cur_i, cur_j = left-cur_len, right+cur_len
            if  not (cur_i>=0 and cur_j < n and s[cur_i] == s[cur_j]):
                break
        return right - left + 2 * cur_len - 1
    
    
    def longestPalindrome(self, s: 'str') -> 'str':
        max_i, max_j = 0,0
        max_len_now = 0
        n = len(s)
        # loop over centers:
        for i in range(n):
            max_len_1 = self.get_max_len(s, i,i)
            # print(i, max_len_1, s[i-max_len_1//2:i+max_len_1//2+1])
            max_len_2 = self.get_max_len(s, i,i+1)
            # print(i, max_len_2,s[i-(max_len_2-1)//2:i+max_len_2//2+1])
            max_len = max(max_len_1, max_len_2)
            if max_len > max_len_now:
                max_i, max_j = i-(max_len-1)//2, i+max_len//2
                max_len_now = max_len
        return s[max_i:max_j+1]
