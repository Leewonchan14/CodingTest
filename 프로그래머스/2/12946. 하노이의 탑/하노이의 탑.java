import java.util.*;

class Solution {
    private static List<int[]> list = new ArrayList();
    
    public int[][] solution(int n) {
        // 옮긴다.
        move(1,3,2,n);
        
        int[][] answer = new int[list.size()][2];
        
        // 컬렉션을 배열으로
        for(int i = 0;i<list.size();i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
    public static void move(int start, int end, int other,int num){
        //만약 옮기는 원판이 한개인 경우 그대로 옮기고 return
        if(num<=1){
            int[] item = new int[]{start, end};
            list.add(item);
            return;
        } 
        
        // 맨아래 원판을 제외한 위 원판을 모두 other로 옮긴후
        move(start, other, end, num-1);
        // 맨아래 원판을 end로
        move(start, end, other, 1);
        // other로 옮긴 원판들 end로 이동
        move(other, end, start, num-1);
            
        return;
        
    }
}