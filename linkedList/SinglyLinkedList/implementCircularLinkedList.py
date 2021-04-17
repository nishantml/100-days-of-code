class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)

        if self.head.next is None:
            self.head = new_node
            self.head.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next

            curr_node.next = new_node;
            new_node.next = self.head
        return self

    def display(self):
        curr = self.head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
            if curr == self.head:
                break
        print(curr.next.val)
        return lst


node = CircularLinkedList()
node.append(10)
node.append(11)
node.append(12)
print(node.display())
