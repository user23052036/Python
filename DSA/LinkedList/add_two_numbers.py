# 2. Add Two Numbers

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(-1)
        mover = dummy

        while l1 or l2:
            total = carry

            if l1:
                total += l1.val
            if l2:
                total += l2.val

            mover.next = ListNode(total % 10)
            mover = mover.next
            carry = total // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            mover.next = ListNode(carry)
        return dummy.next

# Input
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

head1 = createLinkedList(l1)
head2 = createLinkedList(l2)

# Output
obj = Solution()
result = obj.addTwoNumbers(head1, head2)
printLinkedList(result)