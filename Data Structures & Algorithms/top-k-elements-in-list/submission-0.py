class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
    
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num,freq in freqMap.items():
            buckets[freq].append(num)
        
        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        