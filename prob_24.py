# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        dummy = j = ListNode(-1)
        dummy.next = head
        while j  and j.next and j.next.next:
            l = j.next
            r = l.next.next
            l.next.next = l
            j.next = l.next
            l.next = r
            j = l
        return dummy.next

class Solution1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        root = head.next
        while head and head.next:
            L = head
            head = head.next
            R = head.next
            head.next = L
            if R and R.next:
                L.next = R.next
            else:
                L.next = R
            head = R
        return root

        