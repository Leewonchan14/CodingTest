import java.util.stream.*;
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        
        for(int i = 0; i< phone_book.length - 1; i++){
            if(isPre(phone_book[i], phone_book[i+1])){
                return false;
            }
        }
        
        return true;
        
//         Map<String,Integer> map = new HashMap<>();
        
//         for(int i =0 ; i < phone_book.length; i++){
//             String key = phone_book[i] + "0".repeat(20 - phone_book[i].length());
//             System.out.println(key);
//             if(map.containsKey(key))
//                 return false;
            
//             map.put(key,0);
//         }
//         return true;
    }
    
    public boolean isPre(String a, String b){
        return a.startsWith(b) || b.startsWith(a);
    }
}