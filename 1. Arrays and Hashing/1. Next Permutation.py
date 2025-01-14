# Problem link: https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind = -1
        # To find the ind number in the array
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break
        # If no ind is found then simply reverse the array
        # Because the array is already in the sorted order
        if ind == -1:
            nums.reverse()
            return nums

        # After finding the ind, we need to find the next closest number to that ind
        # The closest number should be greater than the ind
        # Then swap it
        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # After swapping, simple reverse the remaining array to keep it in increasing order (smallest value)
        nums[ind+1:] = reversed(nums[ind+1:])
        return nums
