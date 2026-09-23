class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)
        longest = 0

        for n in hash_set:

            
            if n - 1 not in hash_set:
                count = 1
                next = n + 1

                while next in hash_set:
                    count += 1
                    next += 1
                
                longest = max(longest,count)


        return longest
                



        