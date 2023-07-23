# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convertToList(listNode):
    result = []

    while listNode is not None:
        result.append(listNode.val)
        listNode = listNode.next

    return result


def toLinkedList(arr):
    head = ListNode()
    cur = head
    for i, n in enumerate(arr):
        cur.val = n
        if i != len(arr) - 1:
            cur.next = ListNode()
            cur = cur.next

    return head


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversedL1 = convertToList(l1)
        reversedL2 = convertToList(l2)
        reversedL1.reverse()
        reversedL2.reverse()

        longerLength = max(len(reversedL1), len(reversedL2))
        reversedL1 = reversedL1 + [0] * (longerLength - len(reversedL1))
        reversedL2 = reversedL2 + [0] * (longerLength - len(reversedL2))

        answer = []

        carry = 0
        for i in range(longerLength):
            sum = reversedL1[i] + reversedL2[i] + carry
            answer.append(sum % 10)
            carry = sum // 10

        if carry:
            answer.append(carry)

        answer.reverse()
        return toLinkedList(answer)

