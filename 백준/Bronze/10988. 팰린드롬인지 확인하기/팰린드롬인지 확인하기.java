import java.util.*;
import java.util.stream.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        LinkedList<String> list = new LinkedList();
        String str = sc.next();
        for (String s : str.split("")){
            list.addFirst(s);
        }
        String reverse = String.join("", list);
        if(str.equals(reverse)){
            System.out.println(1);
        } else{
            System.out.println(0);
        }
    }
}