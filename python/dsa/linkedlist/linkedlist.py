class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traversal(head):
        while head:
            print(f'{head.data}')
            head = head.next


head = Node(9)
second = Node(7)
third = Node(0)

head.next  = second
second.next = third

Node.traversal(head)