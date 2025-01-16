# Problem link: https://leetcode.com/problems/maximum-subarray/description/

# Optimal Solution - Time complexity: O(n) & Space complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
            if sum_nums > maxi:
                maxi = sum_nums
            # If sum of numbers is a negative number, we simply ignore
            # And start from non-negative numbers by making sum as 0
            if sum_nums < 0:
                sum_nums = 0
        return maxi
