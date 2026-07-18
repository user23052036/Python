# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        mover = dummy
        ptr1 = list1
        ptr2 = list2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                mover.next = ptr1
                ptr1 = ptr1.next
            else:
                mover.next = ptr2
                ptr2 = ptr2.next
            mover = mover.next
        if ptr1:
            mover.next = ptr1
        if ptr2:
            mover.next = ptr2
        return dummy.next
