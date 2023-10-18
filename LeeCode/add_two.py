# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = 1
        a = l1.val * 10 ** (i - 1)
        while (l1.next != None):
            i += 1
            l1 = l1.next
            a += l1.val * 10 ** (i - 1)
        j = 1
        b = l2.val * 10 ** (i - 1)
        while (l2.next != None):
            j += 1
            l2 = l2.next
            b += l2.val * 10 ** (j - 1)
        c = a + b
