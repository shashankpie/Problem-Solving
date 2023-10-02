# Problem link: https://leetcode.com/problems/maximum-subarray/description/

# Optimal Solution - Time complexity: O(n) & Space complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        sum_total = 0
        for i in range(len(nums)):
            sum_total = sum_total + nums[i]
            if sum_total > maxi:
                maxi = sum_total
            if sum_total < 0:
                sum_total = 0
        return maxi
