# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# need to becareful, may have one more digit

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        inc = 0 # if add 
        res_head_k = ListNode(0)
        res_head = res_head_k
        while l1 or l2:
            # get number 1
            if l1:
                left = l1.val
                l1 = l1.next
            else:
                left = 0
            # get number 2
            if l2:
                right = l2.val
                l2 = l2.next
            else:
                right = 0
            res_cur = left + right + inc
            inc = 1 if res_cur > 9 else 0
            res_head.val = res_cur%10
            if l1 or l2:
                res_head.next = ListNode(0)
                res_head = res_head.next
        if inc > 0:
            res_head.next = ListNode(1)
        return res_head_k
        
        