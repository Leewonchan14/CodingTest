class Solution {
    
    int sum = 0;
    int count = 0;

    public int solution(int n) {
        int index = 1;
        while(sum < n){
            // 홀수개로 만들어야 한다면
            if(index % 2 != 0){
                // index 나누어 진다면 count++1;
                if(n % index == 0){
                    count++;
                }
            } 
            // 짝수개로 만들어야 한다면
            else {
                // n-1 % index 0이라면 count ++;
                if((n - index / 2) % index == 0){
                    count++;
                }
            }
            sum += index;  
            index++;
        }
        return count;
        
    }
}