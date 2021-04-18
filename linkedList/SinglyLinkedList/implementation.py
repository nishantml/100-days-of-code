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

    def reverse(self):
        head = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def delete_first_node(self):
        curr = self.head
        if curr.next is None:
            return self
        self.head.next = curr.next.next
        return self

    def delete_last_node(self):
        curr = self.head
        if curr.next is Node:
            return self
        prev = curr
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
        return curr.val

    def move_last_node_to_first(self):
        last_node = self.delete_last_node()
        return self.append_to_head_node(last_node)

    def delete_at_index(self, index):
        curr = self.head
        if curr.next is Node:
            return self
        count = 1
        while curr.next is not None:
            prev = curr
            curr = curr.next
            if count == index:
                prev.next = curr.next
                return self
            count += 1
        return self

    def delete_duplicate(self):
        curr = self.head
        if curr.next is None or curr is None:
            return self
        lst = []
        curr = curr.next
        while curr.next is not None:
            if curr.next.val in lst:
                curr.next = curr.next.next
            else:
                lst.append(curr.next.val)
                curr = curr.next
        return self

    def delete_duplicate_in_sorted(self):
        curr = self.head
        if curr.next is None:
            return self
        curr = curr.next
        while curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

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

    def check_palindrome(self):
        lst = self.display()
        num = 0
        num = int("".join(map(str, lst)))
        rev = int("".join(map(str, reversed(lst))))

        if num == rev:
            return True
        else:
            return False



node = LinkedList()
# node.append_to_tail_node(10)
# node.append_to_tail_node(10)
# node.append_to_tail_node(10)
# node.append_to_tail_node(11)
# node.append_to_tail_node(12)
# node.append_to_tail_node(12)
# node.append_to_tail_node(12)
node.append_to_head_node(9)
node.append_to_head_node(9)
node.append_to_head_node(9)
node.append_to_head_node(8)
node.append_to_head_node(9)
node.append_to_head_node(9)
node.append_to_head_node(9)
# node.delete_first_node()
# node.delete_first_node()
# node.delete_last_node()
# node.delete_last_node()
# node.delete_last_node()
# print(node.display())
# node.delete_at_index(6)
# node.reverse()
# print(node.delete_duplicate_in_sorted())
# print(node.delete_duplicate())
# print(node.display())
# print(node.move_last_node_to_first())
print(node.display())
print(node.check_palindrome())

# print(node.data_at_index(2))
