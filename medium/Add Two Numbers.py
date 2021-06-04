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
            result = f"{result} -> {str(el.val)}"
            el = el.next
        return result

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

class Tester:
    def __init__(self) -> None:
        self.examples = [
            ([2,4,3], [5,6,4], [7,0,8]),
            ([0], [0], [0]),
            ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
        ]
    
    def compare(self, lst1:ListNode, lst2:ListNode) -> bool:
        return str(lst1) == str(lst2)

    def test(self) -> bool:
        all_tests_result = True
        for l1, l2, reference in self.examples:
            result = Solution.addTwoNumbers(l1, l2)
            test_result = self.compare(reference, result)
            all_tests_result = min(all_tests_result, test_result)
            print(f"{'PASS' if test_result else 'FAIL'}\ttwoSum({nums}, {target}) = {result} (reference: {reference})")
        return all_tests_result

t  = Tester()
t.test()