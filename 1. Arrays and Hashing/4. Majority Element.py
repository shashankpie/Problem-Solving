# Problem link: https://leetcode.com/problems/majority-element-ii/description/

# Brute force Solution
# Time complexity - O(n^2)
# Space complexity - O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if len(res) == 0 or res[0] != nums[i]:
                cnt = 0
                for j in range(len(nums)):
                    if nums[i] == nums[j]:
                        cnt += 1
                if cnt > (len(nums) // 3):
                    res.append(nums[i])
            if len(res) == 2:
                break
        return res

# Better Solution
# Time complexity - O(n)
# Space complexity - O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        res = []
        for num, count in hashmap.items():
            if count > (len(nums) // 3):
                res.append(num)
        return res
