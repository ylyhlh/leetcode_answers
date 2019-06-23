# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        if digits=='':
            return []
        dic={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        result = ['']
        for i in range(len(digits)):
            temp = []
            for j in dic[int(digits[i])]:
                for k in result:
                    k=k+j
                    temp.append(k)
            result=temp
        return result