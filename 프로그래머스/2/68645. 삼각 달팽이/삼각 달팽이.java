class Solution {
    int total = 0;
    int num = 0;

    public int[] solution(int n) {
        int total = (n * (n + 1)) / 2;

        int[][] row_col = new int[n][];

        for (int i = 0; i < row_col.length; i++) {
            row_col[i] = new int[i + 1];
        }


        int row = 0;
        int col = 0;
        int count = 1;

        while (count <= total) {
            // 끝까지 아래로
            while(true){
                row_col[row++][col] = count;
                count++;

                // row가 배열의 크기를 넘거나 , 이미 값이 있다면 오른쪽으로 갈준비 하고 break
                if (row >= n || row_col[row][col] > 0) {
                    row--;
                    col++;
                    break;
                }
            }
            
            if(count>total) break;

            // 끝까지 오른쪽
            while(true){
                row_col[row][col++] = count;
                count++;

                // col이 배열의 크기를 넘거나 , 이미 값이 있다면 위로 갈준비를 하고 break
                if (col >= row_col[row].length || row_col[row][col] > 0) {
                    col -= 2;
                    row--;
                    break;
                }
            }
            
            if(count>total) break;

            // 끝까지 위쪽
            while(true){
                row_col[row--][col--] = count;
                count++;

                // row가 배열의 크기를 넘거나 , 이미 값이 있다면 아래로 갈준비를 하고 break
                if (row < 0 || row_col[row][col] > 0) {
                    col++;
                    row+=2;
                    break;
                }
            }
        }

        int[] answer = new int[total];

        int value = 0;
        for (int i = 0; i < row_col.length; i++) {
            for (int j = 0; j < row_col[i].length; j++) {
                answer[value++] = row_col[i][j];
            }
        }

        return answer;
    }
}