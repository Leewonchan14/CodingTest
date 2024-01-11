package Time_2024Y_01M;

public class 시소_짝꿍 {
    public static long solution(int[] weights) {
        int[] countArray = new int[4001];
        long answer = 0;

        // 모든 weight 를 count
        for (int i = 0; i < weights.length; i++) {
            countArray[weights[i]]++;
        }

        for (int weight = 0; weight < countArray.length; weight++) {
            int weightCount = countArray[weight];

            if (weightCount == 0)
                continue;

            // 본인끼리 만나는 경우
            answer += ((long) weightCount * (weightCount - 1));

            // 4/2 경우 조사
            int weight42_Count = countArray[weight * 2];
            if (weight42_Count >= 1) {
                answer += (long) weight42_Count * weightCount;
            }

            // 3/2 , 2 / 4 경우 조사
            if (weight % 2 == 0) {
                // 3/2
                int weight32_Count = countArray[weight * 3 / 2];
                if (weight32_Count >= 1) {
                    answer += (long) weight32_Count * weightCount;
                }
                // 2/4
                int weight24_Count = countArray[weight / 2];
                if (weight24_Count >= 1) {
                    answer += (long) weight24_Count * weightCount;
                }
            }

            // 3/4 경우 조사
            if (weight % 4 == 0) {
                int weight34_Count = weight * 3 / 4;
                if (countArray[weight34_Count] >= 1) {
                    answer += (long) countArray[weight34_Count] * weightCount;
                }
            }

            // 2/3 , 4/3 경우 조사
            if (weight % 3 == 0) {
                // 2/3
                int weight23_Count = weight * 2 / 3;
                if (countArray[weight23_Count] >= 1) {
                    answer += (long) countArray[weight23_Count] * weightCount;
                }
                // 4/3
                int weight43_Count = weight * 4 / 3;
                if (countArray[weight43_Count] >= 1) {
                    answer += (long) countArray[weight43_Count] * weightCount;
                }
            }
        }
        // 중복 제거
        return answer / 2;
    }
}
