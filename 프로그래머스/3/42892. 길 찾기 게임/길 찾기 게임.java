import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;

class Node{
    public int value;
    public int num;
    public Node left;
    public Node right;

    public Node(int value, int num) {
        this.value = value;
        this.num = num;
    }

    @Override
    public String toString() {
        return "Node{" +
                "value=" + value +
                ", num=" + num +
                '}';
    }
}



class Solution {
    public Node insert(Node parentNode, Node newNode){
        if (parentNode == null) {
            return newNode;
        }

        if(newNode.value < parentNode.value){
            parentNode.left = insert(parentNode.left, newNode);
        }else{
            parentNode.right = insert(parentNode.right, newNode);
        }

        return parentNode;
    }

    public List<Integer> preList = new ArrayList<>();
    public List<Integer> postList = new ArrayList<>();

    public void preOrder(Node root){
        if (root == null) {
            return;
        }
        preList.add(root.num);
        preOrder(root.left);
        preOrder(root.right);
    }

    public void postOrder(Node root) {
        if (root == null) {
            return;
        }
        postOrder(root.left);
        postOrder(root.right);
        postList.add(root.num);
    }

    public int[][] solution(int[][] nodeinfo) {
        for (int i = 0; i < nodeinfo.length; i++) {
            nodeinfo[i] = new int[]{i + 1, nodeinfo[i][0], nodeinfo[i][1]};
        }

        LinkedList<int[]> list = Arrays.stream(nodeinfo)
                .sorted(Comparator.comparing((int[] s) -> -s[2]).thenComparing(s -> s[1]))
                .collect(Collectors.toCollection(LinkedList::new));


        Node root = null;
        while (!list.isEmpty()) {
            int[] ints = list.pollFirst();
            root = insert(root, new Node(ints[1], ints[0]));
        }

        preOrder(root);
        postOrder(root);

        return new int[][]{preList.stream().mapToInt(i -> i).toArray(), postList.stream().mapToInt(i -> i).toArray()};
    }
}