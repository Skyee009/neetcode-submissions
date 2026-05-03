class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:

            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        arr = sorted(count, key = count.get, reverse = True)

        return arr[:k]        

        