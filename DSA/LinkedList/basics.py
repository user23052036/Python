class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_front(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    # Delete first occurrence of a value
    def delete(self, val):
        if self.head is None:
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    # Search
    def search(self, val):
        curr = self.head

        while curr:
            if curr.val == val:
                return True
            curr = curr.next

        return False

    # Print list
    def display(self):
        curr = self.head

        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("None")




ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_front(5)

ll.display()
# 5 -> 10 -> 20 -> 30 -> None

print(ll.search(20))
# True

ll.delete(20)

ll.display()
# 5 -> 10 -> 30 -> None