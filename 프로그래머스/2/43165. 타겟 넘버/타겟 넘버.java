class Solution {
    public int solution(int[] numbers, int target) {
        int count = 0;
        
        
        for(int i = 0; i< (int)(Math.pow(2,numbers.length) - 1); i++){
            String bin = Integer.toBinaryString(i);
            
            String zeros = "0".repeat(numbers.length - bin.length());
            
            char[] chars = (zeros + bin).toCharArray();
            
            int sum = 0;
            
            for(int j = 0; j < chars.length ; j++){
                sum += chars[j] == '0' ? numbers[j] * -1 : numbers[j];
            }
            
            count += sum == target ? 1 : 0;
        }
        
        return count;
    }
}