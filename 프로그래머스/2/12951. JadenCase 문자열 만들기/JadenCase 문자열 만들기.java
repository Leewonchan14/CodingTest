import java.util.stream.*;
import java.util.*;
class Solution {
    public String solution(String s) {
        // s = "  a  dsd     sd ";
        String trim = s.trim();
        String[] arr = trim.split("[ ]+");
        
        char[] charArr = s.toCharArray();
        
        boolean isF = true;
    
        
        for(int i = 0; i< charArr.length; i++){
            
            // 공백이면 continue;
            if(charArr[i] == ' '){
                isF = true;
                continue;
            }
            
            // 숫자면
            if('0'<= charArr[i] && charArr[i] <= '9'){
                isF = false;
                continue;
            }
            
            //첫문자가 아니면 소문자로
            if(!isF){
                isF = false;
                charArr[i] = String.valueOf((char)charArr[i]).toLowerCase().charAt(0);
            }
            
            // 첫문자이면 문조건 대문자로
            if(isF){
                isF = false;
                charArr[i] = String.valueOf((char)charArr[i]).toUpperCase().charAt(0);
            }
        }
        
        return String.valueOf(charArr);
    }
}