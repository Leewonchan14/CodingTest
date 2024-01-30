import java.util.stream.*;
import java.util.*;
class Solution {
    
    HashMap<String, Integer> map = new HashMap<>();
    HashMap<String, Integer> carFee = new HashMap<>();
    
    public int[] solution(int[] fees, String[] records) {
        for(String str : records){
            String[] split = str.split(" ");
            
            String[] hour_minute = split[0].split(":");
            
            int hour = Integer.parseInt(hour_minute[0]);
            int minute = Integer.parseInt(hour_minute[1]);
            int time = 60 * hour + minute;
            
            String carNum = split[1];
            
            // 만약 입차라면
            if(!map.containsKey(carNum)){
                // 차량 입차시간 등록
                map.put(carNum, time);
                continue;
            
            }
            
            // 출차 라면
            int inTime = map.remove(carNum);
            // 누적시간 등록            
            carFee.put(carNum, carFee.getOrDefault(carNum, 0) + time - inTime);
        }
        
        // 남은 차 다 출차 하기
        int outTime = 23 * 60 + 59;
        for(String car : map.keySet()){
            carFee.put(car, carFee.getOrDefault(car, 0) + outTime - map.get(car));
        }
        
        return carFee.entrySet().stream().sorted(Map.Entry.comparingByKey()).mapToInt(entry -> {
            int time = entry.getValue();
            if(fees[0] > time){
                return fees[1];
            }

            int addYo = (time - fees[0]) / fees[2];
            addYo += (time - fees[0]) % fees[2] == 0 ? 0 : 1;

            return fees[1] + addYo * fees[3];
        }).toArray();
    }
}