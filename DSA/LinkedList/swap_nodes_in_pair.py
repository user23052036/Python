# 24. Swap Nodes in Pairs

"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without 
modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# my solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        prev = head
        curr = head.next
        nxt = curr.next
        new_head =curr

        while curr:
            curr.next = prev
            if nxt==None or nxt.next==None:
                prev.next = nxt
                break
            else:
                prev.next = nxt.next
            
            curr = prev.next
            prev = nxt
            nxt = curr.next
        return new_head