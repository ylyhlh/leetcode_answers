# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/

# solution 1: recursive slow solution
class Solution_0(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if pattern is empty then, return true is s is missing else return false
        if not p: return not s
        
        #if not s and p: return False
        first_match = bool(s) and p[0] in {s[0], '.'}
        

        # check if * is first pattern
        if len(p)>=2  and p[1] == '*':
            return  ( self.isMatch(s, p[2:])   or first_match and self.isMatch(s[1:], p) )
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# solution 2: dynamic programming
class Solution:
    def isMatch(self, s, p):
        memo = {}
        
        def dp_f(i, j) :
            """ the function to do dynamic programming, if memory has this then return if not calculate"""
            if (i,j) not in memo:

                # trivia cases, pattern is empty 
                if j == len(p):
                    ans = i == len(s)
                else:
                    # if the pattern starting with a*
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp_f(i, j+2) or (first_match and dp_f(i+1, j))
                    else:
                        ans = first_match and dp_f(i+1, j+1)
                memo[(i, j)] = ans
            return memo[(i, j)]
        return dp_f(0,0)
            