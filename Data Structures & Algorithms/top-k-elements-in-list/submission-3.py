from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap: dict = {}
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        heap: list = []
        for num, freq in freqMap.items():
            heappush(heap, [freq, num])
            if len(heap) > k:
                heappop(heap)
        return [num for freq, num in heap]

        