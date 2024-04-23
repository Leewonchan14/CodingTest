import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int[] array) {
        return Arrays.stream(array).sorted()
            .skip(array.length / 2)
            .limit(1).findFirst().orElse(0);
        // return array[array.length / 2];
    }
}