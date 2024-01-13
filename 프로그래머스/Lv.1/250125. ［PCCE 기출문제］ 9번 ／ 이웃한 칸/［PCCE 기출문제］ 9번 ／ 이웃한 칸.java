class Solution {
    public int solution(String[][] board, int h, int w) {
        int minH = 0;
        int maxH = board.length - 1;
        
        int minW = 0;
        int maxW = board[0].length - 1;
        
        int[][] HW = new int[][]{{0,1},{0,-1},{-1,0}, {1,0}};
        
        String targetColor = board[h][w];
        
        int answer = 0;
        
        for(int i = 0;i < 4; i++){
            int searchH = h + HW[i][0];
            int searchW = w + HW[i][1];
            
            if(minH <= searchH && searchH <= maxH 
               && minW <= searchW && searchW <= maxW){
                
                // 같은 색이면
                if(board[searchH][searchW].equals(targetColor))
                    answer++;
            }
            
        }
        
        return answer;
    }
}