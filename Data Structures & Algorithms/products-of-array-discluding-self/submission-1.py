class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        sufix = 1
        output = []


        

        for i in range(len(nums)):
            if i == 0:
                output.append(1)
            else:
                prefix = prefix * nums[i - 1]
                output.append(prefix)



        for i in range(len(nums) - 1, -1 ,-1):
                output[i] = output[i] * sufix
                sufix = sufix * nums[i]
            
        return output

        

        

        