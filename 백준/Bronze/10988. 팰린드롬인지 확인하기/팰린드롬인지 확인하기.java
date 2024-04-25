import java.util.*;
import java.util.stream.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char[] chars = new char[str.length()];
        for (int i = 0; i < str.length(); i ++){
            chars[i] = str.charAt(str.length() - i - 1);
        }
        String reverse = String.valueOf(chars);
        if(str.equals(reverse)){
            System.out.println(1);
        } else{
            System.out.println(0);
        }
    }
}