# Problem link: https://leetcode.com/problems/3sum/description/

# Better Approach - O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st = set()
        for i in range(len(nums)):
            hashmap = set()
            for j in range(i+1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in hashmap:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    st.add(tuple(temp))
                hashmap.add(nums[j])
        ans = list(st)
        return ans

# Optimal Approach - O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if (i != 0 and nums[i] == nums[i-1]):
                continue # if preceding number and current number is same, then increment the i and don't go below
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                total_sum = nums[i] + nums[j] + nums[k]
                if (total_sum < 0):
                    j += 1
                elif (total_sum > 0):
                    k -= 1
                else:
                    # We found the triplets
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    # If the preceding number and current number is same
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1
                    while (j < k and nums[k] == nums[k+1]):
                        k -= 1
        return ans
