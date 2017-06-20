class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_list(cls, list):
        header = None
        prev = None
        for val in list:
            cur = cls(val)
            if not header:
                header = cur
                prev = cur
            else:
                prev.next = cur
                prev = cur
        return header

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        prev = None
        p = 0
        while l1 and l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += p
            cur = ListNode(sum%10)
            if prev:
                prev.next = cur
            else:
                prev = cur
                result = cur
            p = sum/10
        return result


list1 = ListNode.create_list([2,4,3])
list2 = ListNode.create_list([5,6,4])
result = Solution.addTwoNumbers(list1, list2)
print 'test'