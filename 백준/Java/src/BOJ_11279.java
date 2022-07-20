import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class BOJ_11279 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> heapq = new PriorityQueue<>(((o1, o2) -> o2 - o1));

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int cur = Integer.parseInt(br.readLine());
            if (cur == 0) {
                if (heapq.size() == 0) {
                    System.out.println(0);
                } else {
                    System.out.println(heapq.poll());
                }
            } else {
                heapq.add(cur);
            }
        }
    }
}
