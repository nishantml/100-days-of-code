class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append_to_tail_node(self, data):
        curr = self
        new = Node(data)

        while curr.next is not None:
            curr = curr.next
        curr.next = new
        return self

    def display(self):
        curr = self
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst


node = Node(10)
node.append_to_tail_node(11)
node.append_to_tail_node(12)
print(node.display())
