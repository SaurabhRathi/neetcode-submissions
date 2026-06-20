class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] if 1 <= nums[i] <= n else n+1

        for i in range(n):
            val = abs(nums[i])
            if val <= n and nums[val-1] > 0:
                nums[val-1] = -nums[val-1]

        for i in range (n):
            if nums[i] > 0:
                return i+1
        
        return n + 1
 
