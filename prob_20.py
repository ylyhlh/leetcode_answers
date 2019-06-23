# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# nothing much just how to write cleaner/shorter code
class Solution:
    def isValid(self, s: str) -> bool:
        parent_queue = []
        parent_map = {'[':']', '(': ')', '{':'}'}
        for c in s:
            # print(c, parent_queue)
            if c in parent_map:
                parent_queue.append(parent_map[c])
            elif len(parent_queue)==0 or parent_queue.pop() != c:
                    return False
        return len(parent_queue) == 0