# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = 0
        a = 0
        while l1:
            i += 1
            l1 = l1.next
            a += l1.val * 10 ** (i - 1)
        j = 0
        b = 0
        while l2:
            j += 1
            l2 = l2.next
            b += l2.val * 10 ** (j - 1)
        c = a + b


class Solution_1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = head = ListNode()
        bit = 0
        while l1 or l2 or bit:
            curr.next = ListNode()
            curr.val = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + bit) % 10
            bit = curr.val // 10
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next
