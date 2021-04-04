class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def append_to_tail_node(self, data):
        curr = self.head
        new = Node(data)

        while curr.next is not None:
            curr = curr.next
        curr.next = new
        return self

    def append_to_head_node(self, data):
        curr = self.head
        new = Node(data)
        if self.head.next is None:
            self.head.next = new
            return self
        temp = self.head.next
        self.head.next = new
        new.next = temp

        return self

    def delete_first_node(self):
        curr = self.head
        if curr.next is None:
            return self
        self.head.next = curr.next.next
        return self

    def data_at_index(self, index):
        cur_node = self.head
        count = 1
        while cur_node.next is not None:
            cur_node = cur_node.next
            if count == index:
                return cur_node.val
            count += 1
        return -1

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.val)
        return elems


node = LinkedList()
node.append_to_tail_node(10)
node.append_to_tail_node(11)
node.append_to_tail_node(12)
node.append_to_head_node(9)
node.append_to_head_node(8)
node.append_to_head_node(7)

node.delete_first_node()
node.delete_first_node()
print(node.display())

# print(node.data_at_index(2))
