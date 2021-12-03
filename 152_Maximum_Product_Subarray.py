## Note: O(n^2) Brute Force time limit exceeded

'''
Dynamic Programming O(n)--> Time O(1) --> Space
Consider negative number and 0

max product may be produced through:

<1> min_so_far*current number
<2> max_so_far * current number
<3> a subarray starting from current number
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result