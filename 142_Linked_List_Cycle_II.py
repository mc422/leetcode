# 142. Linked List Cycle II

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    x = head
    y = head.next
    while x is not None and y is not None and x != y:
        x = x.next
        if y.next:
            y = y.next.next
        else:
            y = y.next
    if y is None:
        return None
    new = head
    while new != x:
        new = new.next
        x = x.next
    return next


one = ListNode(1)
two = ListNode(2)
one.next = two
print detectCycle(one)
