# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes=[]
        point = head= ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l=l.next
        
        for i in sorted(nodes):
            node=ListNode(i)
            point.next= node
            point=point.next
        return head.next


from heapq import heappush, heappop, heapreplace, heapify
class Solution_0(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node_cur = dummy = ListNode(-1)
        q = [(v.val, v) for v in lists if v]
        heapify(q)
        
        while q: 
            val, node = q [0]
            if node.next is None:
                heappop(q)
            else:
                heapreplace(q, (node.next.val, node.next))
            node_cur.next = node
            node_cur = node_cur.next
            
        return dummy.next
