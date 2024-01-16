import java.util.stream.*;
import java.util.*;

class Solution {    
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList();
        
        int day = 0;
        
        int sameDayDeployCount = 0;
        
        for(int i = 0; i< progresses.length;i++){
            int speed = speeds[i];
            
            int progress = progresses[i] + day*speed;
            
            // 만약 이미 100% 가 넘었다면
            if(progress >= 100){
                sameDayDeployCount++;
                continue;
            }
            
            // 만약 아직 100%가 안됐다면
            if(progress < 100){
                // sameDayDeployCount 가 0 보다 크다면
                if(sameDayDeployCount > 0){
                    answer.add(sameDayDeployCount);
                    sameDayDeployCount = 0;
                }
            }
            
            
            // progress 몇일 걸리는지
            while(progress < 100){
                progress += speed;
                day++;
            }
            
            // 배포되는 기능 하나 추가
            sameDayDeployCount++;
        }
        
        // sameDayDeployCount 가 0 보다 크다면
        if(sameDayDeployCount > 0){
            answer.add(sameDayDeployCount);
        }
        
        int[] answer2 = new int[answer.size()];
        for(int i = 0; i< answer.size(); i++){
            answer2[i] = answer.get(i);
        }
        
        return answer2;
    }
}