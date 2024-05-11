import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    public static int[] inputs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        inputs = new int[N];
        for (int i = 0; i < N; i++) {
            inputs[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(inputs);

        StringBuilder sb = new StringBuilder();

        for (int i : inputs) {
            sb.append(i);
            sb.append("\n");
        }

        System.out.println(sb);
    }
}