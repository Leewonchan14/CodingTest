import java.util.*;
import java.util.stream.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList();
        List<Integer> re = new ArrayList();
        int sum = 0;
        for (int i = 0; i < 9; i++){
            int a = Integer.parseInt(sc.next());
            sum += a;
            list.add(a);
        }
        
        for (int i : list){
            if (re.size() >= 2) break;
            for (int j: list){
                if (i == j) continue;
                if (sum - i - j == 100){
                    re.add(i);
                    re.add(j);
                    break;
                }
            }
        }
        
        int[] b = list.stream()
            .filter(i -> i != re.get(0) && re.get(1) != i).mapToInt(i -> (int)i)
            .sorted()
            .toArray();
        
        
        for (int i : b){
            System.out.println(i);
        }

    }
}