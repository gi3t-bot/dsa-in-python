# Creating a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Insertion of the node
node1 = Node(4)
node2 = Node(2)
node3 = Node(1)
node4 = Node(5)
node5 = Node(9)
node6 = Node(89)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


head = node1
curr = head
while curr is not None:
    print(curr.data, end = " ")
    curr = curr.next