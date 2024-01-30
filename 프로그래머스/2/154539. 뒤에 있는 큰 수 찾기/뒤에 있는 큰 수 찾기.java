class Solution {
    
    int[] dp;
    int[] arr;
    public int[] solution(int[] numbers) {
        dp = new int[numbers.length];
        arr = numbers;
        
        dp[numbers.length - 1] = -1;
        
        int[] answer = new int[numbers.length];
        answer[numbers.length - 1] = -1;
        
        for(int index = numbers.length - 2; index >= 0 ;index--){
            
            answer[index] = nextBig(index);
        }
        
        return answer;
    }
    
    public int nextBig(int index){        
        
        int tempIndex = index + 1;
        
        while(arr[tempIndex] <= arr[index]){

            if(dp[tempIndex] == -1){
                dp[index] = -1;
                return -1;
            }

            tempIndex = dp[tempIndex];
        }
        
        dp[index] = tempIndex;
        return arr[tempIndex];
    }

}