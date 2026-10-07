class Solution:
    def findMin(self, nums: List[int]) -> int: 

        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            if nums[l + 1] < nums[l]:
                return nums[l + 1]
            if nums[r - 1] > nums[r]:
                return nums[r]

            l += 1
            r -= 1

        return nums[l]
        