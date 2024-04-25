import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        String str = sc.next();
        int index = Integer.parseInt(sc.next());
        
        System.out.println(str.split("")[index - 1]);
    }
}