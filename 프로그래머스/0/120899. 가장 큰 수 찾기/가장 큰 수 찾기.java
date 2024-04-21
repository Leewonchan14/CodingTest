class Solution {
    public int[] solution(int[] array) {
        int[] min = {0,1001};
        int[] max = {-1, 0};
        for(int i = 0; i < array.length; i++){
            if(array[i] < min[1]){
                min[1] = array[i];
                min[0] = i;
            }
            if(array[i] > max[0]){
                max[0] = array[i];
                max[1] = i;
            }
        }
        int[] result = {max[0], max[1]};
        return result;
        
    }
}