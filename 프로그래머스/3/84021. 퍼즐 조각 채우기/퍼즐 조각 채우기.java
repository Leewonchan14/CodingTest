import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;

class Table {
    public int cnt;
    public int row;
    public int column;
    public int[][] data;

    public Table spinning() {
        int[][] newData = new int[column][row];
        for (int r = 0; r < column; r++) {
            for (int c = 0; c < row; c++) {
                newData[r][c] = data[c][column - 1 - r];
            }
        }

        return new Table(newData, column, row, cnt);
    }

    public boolean equals(Table other) {
        Table spin1 = other.spinning();
        Table spin2 = spin1.spinning();
        Table spin3 = spin2.spinning();

        return (this.compare(other) || this.compare(spin1) || this.compare(spin2) || this.compare(spin3));
    }

    public boolean compare(Table other) {
        if (row != other.row || column != other.column) {
            return false;
        }

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < column; c++) {
                if (data[r][c] != other.data[r][c]) {
                    return false;
                }
            }
        }

        return true;
    }

    @Override
    public String toString() {
        return "Table{" +
                "cnt=" + cnt +
                ", row=" + row +
                ", column=" + column +
                ", data=" + Arrays.toString(data) +
                '}';
    }

    public Table(int[][] data, int row, int column, int cnt) {
        this.data = data;
        this.row = row;
        this.column = column;
        this.cnt = cnt;
    }

    public Table(int y, int x, int[][] visited, int[][] table, int target) {
        LinkedList<int[]> queue = new LinkedList<>();
        ArrayList<int[]> puzzle = new ArrayList<>();
        queue.addLast(new int[]{y, x});
        visited[y][x] = 1;
        int[] dy = new int[]{0, -1, 0, 1};
        int[] dx = new int[]{-1, 0, 1, 0};

        int minY = y;
        int maxY = y;
        int minX = x;
        int maxX = x;

        while (!queue.isEmpty()) {
            int[] ints = queue.pollFirst();
            cnt += 1;
            y = ints[0];
            x = ints[1];

            puzzle.add(ints);

            minY = Math.min(minY, y);
            maxY = Math.max(maxY, y);
            minX = Math.min(minX, x);
            maxX = Math.max(maxX, x);

            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];


                if (!(0 <= ny && ny < table.length && 0 <= nx && nx < table[0].length)) continue;

                if (visited[ny][nx] == 1 || table[ny][nx] != target) continue;

                visited[ny][nx] = 1;
                queue.addLast(new int[]{ny, nx});
            }
        }

        row = maxY - minY + 1;
        column = maxX - minX + 1;
        data = new int[row][column];

        for (int[] ints : puzzle) {
            int r = ints[0];
            int c = ints[1];

            data[r - minY][c - minX] = 1;
        }
    }
}

class Solution {
    public int solution(int[][] game_board, int[][] table) {
        int[][] visitedA = new int[game_board.length][game_board[0].length];
        int[][] visitedB = new int[table.length][table[0].length];

        ArrayList<Table> blank = new ArrayList<>();
        ArrayList<Table> puzzle = new ArrayList<>();

        for (int r = 0; r < game_board.length; r++) {
            for (int c = 0; c < game_board[0].length; c++) {
                if (visitedA[r][c] == 0 && game_board[r][c] == 0) {
                    blank.add(new Table(r, c, visitedA, game_board, 0));
                }

                if (visitedB[r][c] == 0 && table[r][c] == 1) {
                    puzzle.add(new Table(r, c, visitedB, table, 1));
                }
            }
        }

        Table[] blankArray = blank.toArray(Table[]::new);
        Table[] puzzleArray = puzzle.toArray(Table[]::new);


        HashSet<Integer> setA = new HashSet<>();
        HashSet<Integer> setB = new HashSet<>();

        int cnt = 0;
        for (int i = 0; i < blankArray.length; i++) {
            for (int j = 0; j < puzzleArray.length; j++) {
                Table b = blankArray[i];
                Table p = puzzleArray[j];

                if (!setA.contains(i) && !setB.contains(j) && b.equals(p)) {
                    setA.add(i);
                    setB.add(j);
                    cnt += b.cnt;
                }
            }
        }
        return cnt;
    }
}