class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = defaultdict(int)

        for n in nums:
            frequencies[n] += 1




        result = [x[0] for x in sorted(frequencies.items(),key=lambda x:x[1],reverse=True)]

        # print(result[0:k])

        return result[0:k]
        