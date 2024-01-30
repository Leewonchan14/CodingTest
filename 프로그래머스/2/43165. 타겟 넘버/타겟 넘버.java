class Solution {
    private int[] arr;
    private int tar;
    private int count = 0;

    public int solution(int[] numbers, int target) {
        arr = numbers;
        tar = target;

        dfs(0, 0);

        return count;
    }

    void dfs(int index, int sum) {
        if (index == arr.length) {
            if (sum == tar) {
                count++;
            }
            return;
        }

        dfs(index + 1, sum + arr[index]);
        dfs(index + 1, sum - arr[index]);
    }
}