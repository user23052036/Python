# 92. Reverse Linked List II

"""
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""




# my solution
"""
1. Find the node before the reversal (left_pnt).
2. Find the first node of the reversal (rev_head).
3. Find the last node (rev_tail).
4. Find the node after the reversal (right_pnt).
5. Reverse the sublist.
6. Reconnect the pointers.
"""
class Solution:
    def reverse_ll(self,head: Optional[ListNode], tail: Optional[ListNode]) -> None: # type: ignore
        prev = None
        curr = head
        after = head.next

        while curr != tail:
            curr.next = prev
            prev = curr
            curr = after
            after = curr.next
        curr.next = prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: # type: ignore

        if right==left:
            return head

        # all i need to figure out is to place the left_pnt and right_pnt to before 
        # and after chain reversal node
        temp = head

        cnt = right-left
        temp_left = left-2
        temp_right = right

        if temp_left == -1:
            left_pnt = None
            rev_head = temp

        elif temp_left == 0:
            left_pnt = temp
            rev_head = temp.next

        else:
            while temp_left:
                temp = temp.next
                temp_left -= 1
            left_pnt = temp
            rev_head = temp.next
        
        temp = rev_head
        while cnt:
            temp = temp.next
            cnt -= 1
        rev_tail = temp
        right_pnt = temp.next

        # here we will reverse from rev_head to rev_tail
        # then attach left_pnt -> rev_tail 
        # then attack rev_head -> right_pnt
        # and return head if there exist left pointer else return rev_tail
        self.reverse_ll(rev_head,rev_tail)
        rev_head.next = right_pnt
        if left_pnt:
            left_pnt.next = rev_tail
            return head
        return rev_tail



# 1. Dummy Node + Standard Reverse (Recommended)
class Solution:

    def reverse(self, head, tail):
        stop = tail.next
        prev = stop
        curr = head

        while curr != stop:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

    def reverseBetween(self, head, left, right):

        if left == right:
            return head

        dummy = ListNode(0) # type: ignore
        dummy.next = head
        prev_left = dummy

        for _ in range(left-1):
            prev_left = prev_left.next
        sub_head = prev_left.next
        sub_tail = sub_head

        for _ in range(right - left):
            sub_tail = sub_tail.next
        self.reverse(sub_head, sub_tail)

        prev_left.next = sub_tail
        return dummy.next
    

    
# 2. Head Insertion Technique (Most Elegant)

class Solution:
    def reverseBetween(self, head, left, right):

        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next