# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        curr = head
        lst = []
        while curr.next is not None:
            print(curr.val)
            if curr in lst:
                return True
            lst.append(curr)
            curr = curr.next
        return False


