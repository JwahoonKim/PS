from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getSize(head):
    size = 1

    while head.next is not None:
        head = head.next
        size += 1

    return size


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = getSize(head)

        if size == 1:
            return None

        if n == size:
            return head.next

        prevNode = head
        for i in range(size - n - 1):
            prevNode = prevNode.next

        if prevNode.next is not None:
            prevNode.next = prevNode.next.next
        else:
            prevNode.next = None

        return head
