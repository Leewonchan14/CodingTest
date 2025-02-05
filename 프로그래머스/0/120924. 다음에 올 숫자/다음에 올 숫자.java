class Solution {
    public int solution(int[] common) {
        int d = common[1] - common[0];
        if (d == common[2] - common[1]) {
            return common[common.length - 1] + d;
        }
        return common[common.length - 1] * common[2] / common[1];
    }
}