# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# solution 0: not super clean, need to make dummy node to make this clean
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        if not head:
            return head
        # init 2 pointers
        l = head
        e = head
        for _ in range(n):
            e = e.next

        if not e:
            return head.next
        while e.next:
            l = l.next
            e = e.next
        if l.next:
            l.next = l.next.next
        else:
            return None
        return head
                