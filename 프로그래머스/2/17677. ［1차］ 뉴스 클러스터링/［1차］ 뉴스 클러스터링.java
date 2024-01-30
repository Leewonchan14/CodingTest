import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(String str1, String str2) {
        Map<String, Integer> map1 = makeMap(str1);
        Map<String, Integer> map2 = makeMap(str2);

        HashSet<String> totalKey = new HashSet<>();

        totalKey.addAll(map1.keySet());
        totalKey.addAll(map2.keySet());

        int gyo = 0;
        int hap = 0;

        for (String key : totalKey) {
            boolean isA = map1.containsKey(key);
            boolean isB = map2.containsKey(key);

            if (isA && isB) {
                Integer a = map1.get(key);
                Integer b = map2.get(key);
                gyo += Math.min(a, b);
                hap += Math.max(a, b);
                continue;
            }

            Integer a = map1.getOrDefault(key, 0);
            Integer b = map2.getOrDefault(key, 0);

            hap += Math.max(a, b);
        }
        int result = hap == 0 ? 65536 : (int) ((double) gyo / hap * 65536);
        return result;
    }
    public Map<String, Integer> makeMap(String str) {
        str = str.toLowerCase();

        char[] chars = str.toCharArray();
        HashMap<String, Integer> map = new HashMap<>();

        char[] makeStr = new char[2];

        for (int i = 0; i < chars.length - 1; i++) {
            //둘다 영어 이면
            if (
                    'a' <= chars[i] && chars[i] <= 'z' &&
                            'a' <= chars[i + 1] && chars[i + 1] <= 'z'

            ) {
                makeStr[0] = chars[i];
                makeStr[1] = chars[i + 1];

                String input = String.valueOf(makeStr);

                map.put(input, map.getOrDefault(input, 0) + 1);
            }
        }

        return map;
    }
}