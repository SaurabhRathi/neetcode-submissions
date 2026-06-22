class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        heap = []
        for num, freq in freqMap.items():
            heapq.heappush(heap, [freq, num])
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap] 

        