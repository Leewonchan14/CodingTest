package Time_2024Y_01M;

import java.util.HashMap;
import java.util.Stack;

public class 괄호_회전하기 {
    public static int solution(String s) {

        // 일단 괄호를 매칭시킬 수 있는 Map을 만든다.
        HashMap<String, String> map = new HashMap<>();

        // 그리고 닫힌 괄호를 넣어준다.
        map.put("}", "{");
        map.put("]", "[");
        map.put(")", "(");

        // 정답을 담을 변수를 만든다.
        int answer = 0;

        // 회전시킬 문자열을 담을 변수를 만든다.
        String nowString = s;

        // 입력된 문자열 만큼
        for (int i = 0; i < s.length(); i++) {

            // 문자열을 회전시킨다.
            String spinString = nowString.substring(nowString.length() - 1) + nowString.substring(0, nowString.length() - 1);

            // 문자열의 열린 괄호를 담을 스택을 만든다.
            Stack<String> stack = new Stack<>();

            // 문자열의 길이만큼
            for (int index = 0; index < spinString.length(); index++) {


                // 반복문 현재 문자열의 문자를 가져온다.
                String nowChar = String.valueOf(spinString.charAt(index));

                // 스택이 비어있으면 그냥 넣어주고 문자열을 회전시킨다.
                if (stack.isEmpty()) {
                    stack.add(nowChar);
                    continue;
                }

                // 닫힌 괄호인지 확인한다.
                boolean isClose = map.containsKey(nowChar);

                // 열린 괄호 라면 그냥 넣어주고 문자열을 회전시킨다.
                if (!isClose) {
                    stack.add(nowChar);
                    continue;
                }

                // 닫힌 괄호라면 스택의 맨 위의 괄호를 가져온다.
                String peekChar = stack.peek();

                // 현재 닫힌 괄호가 스택의 맨 위의 괄호와 매핑되는지 확인한다.
                boolean isMapping = map.get(nowChar).equals(peekChar);

                // 매핑되지 않는다면 스택에 넣어주고 문자열을 회전시킨다.
                if (!isMapping) {
                    stack.add(nowChar);
                    continue;
                }

                // 매핑된다면 스택에서 꺼내고 문자열을 회전시킨다.
                stack.pop();
            }

            // 문자열을 회전시켰을 때 스택이 비어있다면 정답을 증가시킨다.
            if (stack.isEmpty()) {
                answer++;
            }

            // 회전시킨 문자열을 다음 문자열로 넣어준다.
            nowString = spinString;
        }

        return answer;
    }
}
