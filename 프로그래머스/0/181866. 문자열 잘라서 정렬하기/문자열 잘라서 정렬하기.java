import java.util.stream.*;
import java.util.*;

class Solution {
    public String[] solution(String myString) {
        return Arrays.stream(myString.split("x")).filter(x -> !x.equals("")).sorted().toArray(String[]::new);
    }
}