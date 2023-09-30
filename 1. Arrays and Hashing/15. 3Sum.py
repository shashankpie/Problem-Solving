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
