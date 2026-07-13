class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return ans