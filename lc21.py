class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoList(self, head1, head2):
        head = ListNode(0)
        first = head
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        if head1 == None:
            head.next = head2
        elif head2 == None:
            head.next = head1

        return first.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(1)
l5 = ListNode(2)
l6 = ListNode(4)
l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6
solution = Solution()
res = solution.mergeTwoList(l1, l4)
while res:
    print(res.val)
    res = res.next