class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        nums.sort()

        

        max = 1
        i = 0

        while i < len(nums) - 1:

            count = 1;

            while (i < len(nums) - 1) and ((nums[i + 1] - nums[i] == 1) or (nums[i + 1] - nums[i] == 0)):
                if (nums[i + 1] - nums[i] == 1):
                    count += 1
                i += 1

            if count > max:
                max = count

            i += 1



        return max

        