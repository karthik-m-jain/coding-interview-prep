"""
Question: 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

1) 2 <= nums.length <= 105
2) -30 <= nums[i] <= 30
3) The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, result = 1, 1, [0 for i in nums]
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
    
sol = Solution()
print(sol.productExceptSelf([-1,1,0,-3,3]))

"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
    1. Maintain two different arrays for prefix and suffix. Space = O(n)
"""