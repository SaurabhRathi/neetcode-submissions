class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {0: 1}
        curr, count = 0, 0
        for num in nums:
            curr += num
            count += sumMap[curr-k] if curr-k in sumMap else 0
            sumMap[curr] = 1 + sumMap[curr] if curr in sumMap else 1
        return count