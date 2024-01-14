import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int[] sequence, int k) {
        int sum = sequence[0];
        int frontIndex = 0;
        int backIndex = 0;
        List<int[]> list = new ArrayList();
        
        while(backIndex < sequence.length){
            int frontValue = sequence[frontIndex];

            // sum이 k 보다 작으면 sum += nextValue;
            if(sum < k){

                // backIndex가 sequence의 마지막 인덱스라면 break
                if (backIndex == sequence.length - 1) {
                    break;
                }

                // backIndex를 증가시키고 sum에 더해준다.
                int nextValue = sequence[backIndex + 1];
                sum += nextValue;

                // backIndex 증가 == sum 오른쪽 증가
                backIndex++;
                continue;
            }

            // sum이 k랑 같다면 front, back을 저장
            if(sum == k){
                list.add(new int[]{frontIndex,backIndex});
            }

            //if frontIndex 가 backIndex 과 같다면 break;
            if(frontIndex == backIndex ){
                break;
            }
            
            //sum 왼쪽 증가 (sum이 k 보다 커도)
            sum -= frontValue;
            frontIndex++;
        }

        // list의 [a,b] b-a의 최솟값을 찾는다.
        int[] minA_B = list.get(0);
        for(int[] a_b : list){
            int a = a_b[0];
            int b = a_b[1];

            int nowGap = b - a;

            int minGap = minA_B[1] - minA_B[0];

            if(minGap > nowGap){
                minA_B[0] = a;
                minA_B[1] = b;
            }
        }
        
        return minA_B;
        
    }
}