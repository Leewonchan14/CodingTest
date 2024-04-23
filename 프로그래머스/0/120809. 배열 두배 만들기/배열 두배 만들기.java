import java.util.stream.*;
import java.util.*;
class Solution {
    public List<Integer> solution(int[] numbers) {
        return Arrays.stream(numbers).mapToObj(i->i*2)
            .collect(Collectors.toList());
    }
}