import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1854 {
    static int n, m, k;
    static List<List<int[]>> adj;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        adj = new ArrayList<>();
        List<List<Integer>> distance = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
            distance.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            adj.get(start).add(new int[] {end, cost});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        pq.add(new int[] {1, 0});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int now = poll[0];
            int cost = poll[1];

            if(distance.get(now).size() >= k) {
                continue;
            }

            distance.get(now).add(cost);
            for (int[] next : adj.get(now)) {
                pq.add(new int[] {next[0], cost + next[1]});
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            List<Integer> dist = distance.get(i);
            if (dist.size() < k) {
                sb.append(-1).append("\n");
            } else {
                sb.append(dist.get(k - 1)).append("\n");
            }
        }
        System.out.println(sb);
    }
}
