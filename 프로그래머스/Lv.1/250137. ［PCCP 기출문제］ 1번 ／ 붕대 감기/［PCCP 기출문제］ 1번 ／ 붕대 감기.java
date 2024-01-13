class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        // 최대 체력
        int maxHealth = health;
        
        //붕대 감기의 시전시간
        int coolTime = bandage[0];
        // 붕대 감기의 초당 회복량
        int healGap = bandage[1];
        // 붕대 감기의 추가 회복량
        int addHeal = bandage[2];
        
        // 맨처음 공격패턴의 데미지, 시간 계산
        int[] preAttack = attacks[0];
        int preTime = preAttack[0];
        int preDamage = preAttack[1];
        
        // 처음 공격 맞기
        health -= preDamage;
        
        //만약 죽으면 return -1;
        if(health <= 0){
            return -1;
        }
        
        
        // attacks 배열을 돌며 각 공격 패턴마다 실행
        for(int i = 1; i < attacks.length; i++){
            // 현재 공격패턴의 time, damage를 계산
            int[] pattern = attacks[i];
            int nowTime = pattern[0];
            int nowDamage = pattern[1];
            
            // 맞기전 회복 먼저
            
            //추가 회복을 감지할 변수 선언
            int comboHealCount = 0;
            
            // 맞기 전 시간과 이전 공격 시간 차이 만큼 회복시킨다.
            // 맞기전 시간 - 이전 공격 시간
            int gapTime = (nowTime - 1) - preTime;
            for(int j = 1; j <= gapTime; j++){
                // 초당 회복
                health += healGap;
                // 콤보 증가
                comboHealCount++;
                
                // 만약 max 콤보라면 추가 힐
                if(comboHealCount >= coolTime){
                    health += addHeal;
                    // 콤보 초기화
                    comboHealCount = 0;
                }
                
                // 최대체력이라면
                if(health >= maxHealth){
                    health = maxHealth;
                }
            }
            
            // 현재 공격 맞기 
            health -= nowDamage;
            
            //만약 죽으면 return -1;
            if(health <= 0){
                return -1;
            }
            
            // 이전 공격 변수 설정
            preTime = nowTime;
            preDamage = nowDamage;
        }
        
        return health;
        
    }
}