class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mini = math.inf
        for i in range(len(nums)):
            nums[i] = nums[i] if nums[i] > 0 else None
            mini = min(mini, nums[i] if nums[i] is not None else math.inf)

        if mini != 1:
            return 1

        for i in range(len(nums)):
            if nums[i] is None or nums[i] == 0:
                continue
            index = (nums[i] if nums[i] > 0 else -nums[i]) - 1
            if index >= len(nums) or (nums[index] is not None and nums[index] < 0):
                continue
            
            nums[index] = -nums[index] if nums[index] is not None else 0

        for i in range (0, len(nums)):
            if nums[i] is None or nums[i] > 0:
                return i+1
        
        return len(nums) + 1
 
