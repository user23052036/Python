# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        if head==None or head.next==None:
            return head
        
        prev = None
        temp = head
        after = head.next

        while after != None:
            temp.next = prev

            prev = temp
            temp = after
            after = temp.next
        temp.next = prev
        return temp