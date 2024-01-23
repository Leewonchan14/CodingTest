import java.util.stream.*;
import java.util.*;
class Solution {
    // 최대 행
    private int maxRow;
    
    // 최대 열
    private int maxColumn;
    
    // Create Queue
    private Queue<Node> que = new LinkedList<>();
    
    public int solution(int[][] maps) {

        maxRow = maps.length - 1;
        maxColumn = maps[0].length - 1;

        // 처음 노드 갔다고 표시하고 Queue에 넣기
        maps[0][0] = 0;
        que.add(new Node(0,0, 1));
        // 정답을 return 할 변수
        int moveCount = 1;

        // Queue가 비어있지 않으면
        while(!que.isEmpty()){

            // Queue에서 하나 뽑기
            Node node = que.poll();

            // MoveCount 가져오기
            moveCount = node.getMoveCount();

            // 만약 목적지에 도착 했다면
            if (node.getRow() == maxRow && node.getCol() == maxColumn){
                return moveCount;
            }

            // 모든 방향 check
            for (Direction dir : Direction.values()) {

                int nextRow = node.getRow() + dir.getRow();
                int nextCol = node.getCol() + dir.getCol();

                // 만약 갈수 있으면
                if(check(nextRow, nextCol, maps)){
                    // 갔다고 체크 후
                    maps[nextRow][nextCol] = 0;
                    // Enqueue
                    que.add(new Node(nextRow, nextCol, moveCount + 1));
                }
            }
        }
        return -1;
    }

    public boolean check(int row, int col, int[][] maps) {
        // 갈수있는지 확인
        if (
                0 <= row && row <= this.maxRow &&
                        0 <= col && col <= this.maxColumn
        ) {
            // 안가봤거나 뚫려있으면
            return maps[row][col] == 1;
        }
        return false;
    }
    
    public class Node {
        private final int row;
        private final int col;
        private final int moveCount;

        public Node(int row, int col, int moveCount) {
            this.row = row;
            this.col = col;
            this.moveCount = moveCount;
        }

        public int getRow() {
            return row;
        }

        public int getCol() {
            return col;
        }

        public int getMoveCount() {
            return moveCount;
        }
    }

    public enum Direction {
        UP(-1, 0), DOWN(1, 0), LEFT(0, -1), RIGHT(0, 1);
        private int row;
        private int col;

        Direction(int row, int col) {
            this.row = row;
            this.col = col;
        }

        public int getRow() {
            return row;
        }

        public int getCol() {
            return col;
        }
    }
}