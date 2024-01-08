package Time_2024Y_01M;

import java.util.Arrays;

public class n제곱_배열_자르기 {
    public static int[] solution(int n, long left, long right) {
        int[] answer = new int[(int) (right - left) + 1];

        for (long i = left; i <= right; i++) {
            // index 를 계산
            int index = (int)(i - left);

            //column 를 계산
            long column = i % n;

            //row 를 계산
            long row = i / n;

            // 만약 column 의 수가 row 보다 크다거나 같다면 column + 1
            if (column >= row) {
                answer[index] = (int)(column + 1);
                continue;
            }

            // 나머지는 row + 1
            answer[index] = (int)(row + 1);
        }

        return answer;
    }

    public static int[] solution_3(int n, long left, long right) {
        int[] answer = new int[(int) (right - left) + 1];

        for (long row = 0; row < n; row++) {
            for (long column = 0; column < n; column++) {
                // 만약 해당하는 인덱스가 left, right에 속해 있지 않다면 continue
                long index = n * row + column;
                if (index < left || index > right) {
                    continue;
                }

                // 속해 있다면 index 계산
                int answerIndex = (int)(index - left);
                // 만약 column 의 수가 row 보다 크다거나 같다면 column + 1 채우기
                if (column >= row) {
                    answer[answerIndex] = (int)(column + 1);
                    continue;
                }

                // 나머지는 row + 1 으로 채우기
                answer[answerIndex] = (int)(row + 1);
            }
        }

        return answer;
    }
    public static int[] solution_2(int n, long left, long right) {
        int[] answer = new int[(int) (right - left) + 1];

        for (long row = 0; row < n; row++) {
            for (long column = 0; column < n; column++) {
                // 만약 해당하는 인덱스가 left, right에 속해 있지 않다면 continue
                long index = n * row + column;
                if (index < left || index > right) {
                    continue;
                }

                // 속해 있다면 index 계산
                int answerIndex = (int)(index - left);
                // 만약 column 의 수가 row 보다 크다거나 같다면 column + 1 채우기
                if (column >= row) {
                    answer[answerIndex] = (int)(column + 1);
                    continue;
                }

                // 나머지는 row + 1 으로 채우기
                answer[answerIndex] = (int)(row + 1);
            }
        }

        return answer;
    }

    public int[] solution_1(int n, long left, long right) {
        int[] array = new int[n * n];

        for (int row = 0; row < n; row++) {
            for (int column = 0; column < n; column++) {
                // 만약 column 의 수가 row 보다 크다거나 같다면 column + 1 채우기
                if (column >= row) {
                    array[n * row + column] = column + 1;
                    continue;
                }

                // 나머지는 row + 1 으로 채우기
                array[n * row + column] = row + 1;
            }
        }

        return Arrays.copyOfRange(array, ((int) left), (int) (right + 1));
    }
}
