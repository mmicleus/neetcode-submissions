class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i,x in enumerate(nums):

            aux = target - x

            if aux in prevMap:
                return [prevMap[aux],i]

            prevMap[x] = i 
        