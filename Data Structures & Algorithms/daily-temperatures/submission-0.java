class Solution {
    public int[] dailyTemperatures(int[] arr) {
        int len = arr.length;
        int[] ans = new int[len];
        Stack<Integer> stack = new Stack<>();
        for(int i=len-1; i>=0; i--) {
            while(stack.size() > 0 && arr[i] >= arr[stack.peek()]) {
                stack.pop();
            }
            ans[i] = stack.size() == 0? 0 : stack.peek() - i;
            stack.add(i);
        }
        return ans;
    }
}
