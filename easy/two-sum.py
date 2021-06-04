# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            delta = target - num
            if delta in nums[i+1:]:
                return [i, nums.index(delta, i+1)]
        return []

class Tester:
    def __init__(self) -> None:
        self.examples = [
            ([2,7,11,15], 9, [0,1]),
            ([3,2,4], 6, [1,2]),
            ([3,3], 6, [0,1])
        ]
    
    def compare(self, lst1:list, lst2:list) -> bool:
        return set(lst1) == set(lst2)

    def test(self) -> bool:
        all_tests_result = True
        for nums, target, reference in self.examples:
            result = Solution.twoSum(nums, target)
            test_result = self.compare(reference, result)
            all_tests_result = min(all_tests_result, test_result)
            print(f"{'PASS' if test_result else 'FAIL'}\ttwoSum({nums}, {target}) = {result} (reference: {reference})")
        return all_tests_result

t  = Tester()
t.examples.append(([2,5,2,3],5,[0,3]))
t.examples.append(([2,5,2,3],9,[]))
t.test()