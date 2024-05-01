class Solution {
    public int[] solution(int n, int s) {
        if (n > s) return new int[] { - 1};
        
        int[] result = new int[n];
        for(int i = 0; i < n; i++){
            result[i] = s / n;
        }
        
        int div = s % n;
        
        for(int i = n - div; i < n; i++){
            result[i]++;
        }
        return result;
    }
}