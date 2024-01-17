class Solution {
    public int solution(int[] people, int limit) {
        People ple = new People(people);
        
        int answer = 0;
        
        int smallWeight = 0;
        
        while(true){
            // 가장 큰 몸무게를 뽑아 온다.
            int bigWeight = ple.pollBigWeight();
            // 만약 0 이 나왔다면 break;
            if(bigWeight == 0) break;
            
            // 가장 작은 몸무게를 가져온다.
            smallWeight = ple.peekSmallWeight();
            
            // 만약 큰무게와 작은 무게가 합쳐서 limit보다 작거나 같다면 태워 보낸다.
            if(bigWeight + smallWeight <= limit){
                answer++;
                ple.pollSmallWeight();
                // 다음 사람 조사
                continue;
            }
            
            // 만약 limit보다 크다면 큰사람만 태워 보낸다.
            answer++;
        }
    
        if(ple.pollSmallWeight() > 0){
            answer++;
        }
        
        return answer;
    }
    
    class People {
        // 모든 무게의 갯수를 담을 배열 선언
        private int[] weightCountArray = new int[241];
        
        private int smallWeight = 0;
        private int bigWeight = 240;
        
        People(int[] people){
            // 무게를 인덱스로 갯수를 count
            for(int index = 0; index<people.length; index++){
                int weight = people[index];
                weightCountArray[weight] += 1;
            }
        }
        
        //가장 큰 무게를 가진 사람의 무게를 peek 하는 메서드
        public int peekBigWeight(){
            int bigWeightCount = weightCountArray[bigWeight];
            
            // count가 존재 할때까지 
            while(bigWeightCount == 0){
                
                bigWeight--;
                // 만약 작은 몸무게 보다 작아졌다면 0을 리턴
                if(bigWeight < smallWeight){
                    return 0;
                }
                bigWeightCount = weightCountArray[bigWeight];
            }
            
            return bigWeight;
        }
        
        //가장 큰 무게를 가진 사람의 무게를 pop하는 메서드
        public int pollBigWeight(){
            // 가장큰 몸무게 가져오기
            bigWeight = peekBigWeight();
            
            // 1제거
            weightCountArray[bigWeight] -= 1;
            
            return bigWeight;
        }
        
        //가장 작은 무게를 가진 사람의 무게를 pop하는 메서드
        public int pollSmallWeight(){
            int smallWeight = peekSmallWeight();
            
            // 1제거
            weightCountArray[smallWeight] -= 1;
            
            return smallWeight;
        }
        
        //가장 작은 무게를 가진 사람의 무게를 peek 하는 메서드
        public int peekSmallWeight(){
            int smallWeightCount = weightCountArray[smallWeight];
            
            // count가 존재 할때까지 
            while(smallWeightCount == 0){
                
                smallWeight++;
                // 만약 큰 몸무게 보다 커졌다면 0을 리턴
                if(bigWeight < smallWeight){
                    return 0;
                }
                
                smallWeightCount = weightCountArray[smallWeight];
            }
            
            return smallWeight;
        }
        
    }
}