class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {0: 1}
        curr, count = 0, 0
        for num in nums:
            curr += num
            count += sumMap.get(curr-k, 0)
            sumMap[curr] = 1 + sumMap.get(curr, 0)
        return count