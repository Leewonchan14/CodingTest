class Solution {
    public int solution(int n, int k) {
        String toStr = Integer.toString(n, k);

        toStr = toStr.replaceAll("[0]+", " ").trim();
        
        int count = 0;

        for (String str : toStr.split(" ")) {
            if (isPrime(Long.parseLong(str))) {
                count++;
            }
        }

        return count;
        
    }
    
    public boolean isPrime(long n){
        if(n <= 1){
            return false;
        }
        
        for (int i = 2; (long) i * i <= n; i++) {
            if (n % i == 0){
                return false;
            }
        }

        return true;
    }
}