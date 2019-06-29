# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/



# instead of taking max to change the value for j and max_len, it is better just use if .
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # left pointers
        if len(s) == 0:
            return 0
        j = 0
        N = len(s)
        max_len = 1
        last_pos_dict = {s[0]: 0}
        for i in range(1, N):
            ch = s[i]
            if ch in last_pos_dict:
                last_pos = last_pos_dict[ch] + 1
                if  last_pos > j:
                    j = last_pos
            last_pos_dict[ch] = i
            cur_len = i - j + 1
            if cur_len > max_len:
                max_len = cur_len
                
        return max_len