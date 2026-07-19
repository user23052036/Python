class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

n1 = ListNode()
# n2 = ListNode(2,n1)
# print('node1 -> ',n1, 'type ->',type(n1))
# print('node2 -> ',n2.next, 'type ->',type(n2.next))
# print('node2 val -> ',n2.val, 'type -> ', type(n2.val))
print(type(n1))
print(type(n1.val))
print(type(n1.next))
