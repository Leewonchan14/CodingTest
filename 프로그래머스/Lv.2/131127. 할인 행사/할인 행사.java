import java.util.stream.*;
import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String,Integer> wantCountMap = new HashMap();
        // init wantCountMap
        for(int i = 0;i<want.length;i++){
            
            String key = want[i];
            
            int count = number[i];
            
            // map에 있으면 있던거에 +1
            //if(wantCountMap.containsKey(key))
                //count = wantCountMap.get(key) + 1;
            
            // map에 넣기
            wantCountMap.put(key, count);
        }
        
        
        // init saleCountMap
        Map<String,Integer> saleCountMap = new HashMap();
        
        for(int i = 0;i<10;i++){
            int count = 1;
            
            String key = discount[i];
            
            // map에 있으면 있던거에 +1
            if(saleCountMap.containsKey(key))
                count = saleCountMap.get(key) + 1;
            
            // map에 넣기
            saleCountMap.put(key, count);
        }
        
        int answer = 0;
        
        Set<String> wantKeys = wantCountMap.keySet();
        
        // 전체 discount 를 돌며 saleCount와 wankCount가 같은지 체크 하고 같으면 +1
        for(int nowIndex = 0; nowIndex < discount.length; nowIndex++){
            // 유효한 key의 갯수를 셀 변수 선언
            int validKeyCount = 0;
            
            // wantCountMap의 key가 모두 saleCount에 있는지 체크
            for(String key : wantKeys){
                boolean isKeyExist = saleCountMap.containsKey(key);
                // 원하는 key가 존재 하지 않는다면 다음 discount 확인하기
                if(!isKeyExist){
                    break;
                }
                
                // 존재 한다면 count 체크
                boolean isCountEqual = 
                    wantCountMap.get(key) == saleCountMap.get(key);
                
                // count가 다르다면 다음 discount 확인하기
                if(!isCountEqual){
                    break;
                }
                
                // 모든 key가 있고 key에 count가 다 같다면 answer+=1
                validKeyCount++;
            }
            
            // 유효한 키갯수와 모든 키 갯수가 같다면 answer += 1
            if(validKeyCount == want.length){
                answer++;
            }
            
            // saleCountMap을 다음걸로 만들어주기
            int outIndex = nowIndex;
            int inIndex = nowIndex + 10;
            
            // 만약 들어오는 인덱스가 범위를 벗어나면 break;
            if(inIndex >= discount.length)
                break;
            
            String outKey = discount[outIndex];
            String inKey = discount[inIndex];
            
            // saleCountMap에 나가는 품목 -1
            int outKeyCount = saleCountMap.get(outKey);
            
            saleCountMap.put(outKey,outKeyCount - 1);
             
            int inKeyCount = 1;
            // 들어오는 품목 있으면 있던거에 +1
            if (saleCountMap.containsKey(inKey))
                inKeyCount = saleCountMap.get(inKey) + 1;
            
            saleCountMap.put(inKey,inKeyCount);
        }
        return answer;
    }
}