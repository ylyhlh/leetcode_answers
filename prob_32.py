# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                # print(stack)
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])
        return max_len

class Solution_0(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_counter = r_counter = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                l_counter +=1
            else:
                r_counter +=1
                if r_counter == l_counter:
                    max_len = max(max_len, l_counter*2)
                elif r_counter > l_counter:
                    l_counter = r_counter = 0
        
        l_counter = r_counter = 0
        for i in range(len(s)-1, -1,-1):
            if s[i] == ')':
                r_counter +=1
            else:
                l_counter +=1
                if r_counter == l_counter:
                    max_len = max(max_len, l_counter*2)
                elif l_counter > r_counter:
                    l_counter = r_counter = 0
        return max_len