import java.util.stream.*;
import java.util.*;
class Solution {
    Map<String[], Integer> visited = new HashMap<>();
    Map<String, List<String[]>> go = new HashMap<>();
    LinkedList<String> ls = new LinkedList<>();
    List<String[]> result = new ArrayList<>();
    public String[] solution(String[][] tickets) {
        for(String[] m : tickets){
            visited.put(m, 0);
            
            List<String[]> gogo = go.getOrDefault(m[0],new ArrayList<>());
            gogo.add(m);
            go.put(m[0], gogo);
        }
        ls.addLast("ICN");
        dfs();
        
        return result.stream()
            .sorted(Comparator.comparing(s -> String.join("",s)))
            .findFirst().get();
    }
    
    public void dfs(){
        if (ls.size() - 1 == visited.size()){
            result.add(ls.stream().toArray(String[]::new));
            return;
        }
        
        for(String[] s: go.getOrDefault(ls.peekLast(), new ArrayList<>())){
            if (visited.get(s) == 1) continue;
            
            visited.put(s, 1);
            ls.addLast(s[1]);
            dfs();
            ls.pollLast();
            visited.put(s, 0);
        }
    }
}