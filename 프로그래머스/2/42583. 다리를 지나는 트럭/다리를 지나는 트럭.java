import java.util.*;
class Solution {
    LinkedList<Integer> brige = new LinkedList();
    LinkedList<Integer> que = new LinkedList();
    int sumWeight = 0;
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        for(int i = 0; i < bridge_length; i++){
            brige.addLast(0);
        }
        
        for(int truck : truck_weights){
            que.addLast(truck);
        }
        
        int time = 0;
        
        while(!que.isEmpty() || sumWeight != 0){
            time += 1;
            int popItem = 0;
            sumWeight -= brige.pollFirst();
            if(!que.isEmpty() && sumWeight + que.peekFirst() <= weight){
                popItem = que.pollFirst();
                sumWeight += popItem;
                brige.addLast(popItem);
            } else{
                brige.addLast(0);
            }
        }
        return time;
    }

}