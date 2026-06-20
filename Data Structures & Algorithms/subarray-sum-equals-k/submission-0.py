class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {}
        sumMap[0] = 1
        curr, count = 0, 0
        for num in nums:
            curr += num
            if curr-k in sumMap:
                count += sumMap[curr-k]

            if curr in sumMap:
                sumMap[curr] += 1
            else:
                sumMap[curr] = 1
        return count