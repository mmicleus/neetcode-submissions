class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux = set(nums)


        return not (len(aux) == len(nums))



