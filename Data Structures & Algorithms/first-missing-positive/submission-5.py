class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i<n:
            index = nums[i]-1
            if index >= n or index < 0 or nums[index] == nums[i]:
                i += 1
            else:
                nums[i], nums[index] = nums[index], nums[i] 
           
        for i in range(n):
            if nums[i]!=i+1:
                return i+1

        return n+1;
