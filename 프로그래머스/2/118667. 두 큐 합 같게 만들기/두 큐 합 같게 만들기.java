import java.util.stream.*;
import java.util.*;
class Solution {        
    public int solution(int[] queue1, int[] queue2) {
        
        // queue1를 담을 Queue
        Squeue que1 = new Squeue(queue1);
        // queue2를 담을 Queue
        Squeue que2 = new Squeue(queue2);
        // 계산 결과를 담을
        long result = 0L;
        
        while(true){
            
            // 1. 만약 Queue의 원소가 하나도 없다면 return
            if(que1.size() <= 0 || que2.size() <= 0){
                return -1;
            }
            
            // 2. sum 대소 비교
            int compare = Long.compare(que1.getSum(), que2.getSum());

            // 3. sum이 같은지 확인하고 같으면 return, 다르면 poll
            if(compare == 0){
                return (int)result;
            }
            
            // 4. 모든 원소를 다 해봤다면 return
            if(result > que1.size() + que2.size() + 1){
                return -1;
            }
            

            // 5. sum이 큰쪽에서 poll을하고 작은 쪽에 넣어준다.
            if(compare == -1){
                // sum2가 크다면 que2 에서 뺀뒤 que1에 넣는다.
                que1.addOther(que2);
            } 
            else if (compare == 1){
                // sum1가 크다면 que1 에서 뺀뒤 que2에 넣는다.
                que2.addOther(que1);
            }
            
            // result 증가
            result++;
        }
    }
    
    class Squeue{
        private Queue<Integer> que = new LinkedList<>();
        
        private long sum = 0L;
        
        
        // 생성자로 초기화
        Squeue(int[] queue){
            for(int i = 0; i < queue.length; i++){
                que.add(queue[i]);
                sum += queue[i];
            }
        }
        
        public long getSum(){
            return sum;
        }
        
        public int size(){
            return que.size();
        }
        
        public int poll(){
            int polling = que.poll();
            sum -= polling;
            return polling;
        }
        
        public void addOther(Squeue other){
            int polling = other.poll();
            
            this.sum += polling;
            
            this.que.add(polling);
        }

    }
}