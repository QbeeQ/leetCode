# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = str(self.val)
        el = self.next
        while el:
            result = f"{result}-{str(el.val)}"
            el = el.next
        return result

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ListNode): return False
        if self.val != o.val: return False
        return self.next == o.next

def addTwoNumbers_off(l1: ListNode, l2: ListNode, up=None) -> ListNode:
    if l1 or l2 or up:
        s = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + (0 if up is None else up)
        res = ListNode(s if s < 10 else s-10)
        res.next = addTwoNumbers_off(
            l1.next if l1 else None,
            l2.next if l2 else None,
            None if s < 10 else 1
        )
        return res

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    res = cur = None
    up = 0
    while l1 or l2 or up > 0:
        if res is None:
            res = cur = ListNode((0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + up)
        else:
            cur.next = ListNode((0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + up)
            cur = cur.next
        if cur.val < 10:
            up = 0
        else:
            up = 1
            cur.val -= 10
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return res

def examples():
    return [
        (
            (
                ListNode(2, ListNode(4, ListNode(3))),
                ListNode(5, ListNode(6, ListNode(4)))
            ),
            ListNode(7, ListNode(0, ListNode(8)))
        ),
        (
            (
                ListNode(0),
                ListNode(0)
            ),
            ListNode(0)
        ),
        (
            (
                ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
            ),
            ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
        )
    ]
