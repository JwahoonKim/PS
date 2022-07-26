import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1753 {
    static int V, E, K;
    static int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        int[] distance = new int[V + 1];
        Arrays.fill(distance, INF);

        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= V; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            adj.get(start).add(new int[] {end, dist});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        pq.add(new int[]{K, 0});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int node = poll[0];
            int dist = poll[1];
            if (distance[node] > dist) {
                distance[node] = dist;
                for (int[] next : adj.get(node)) {
                    if (next[1] + dist < distance[next[0]])
                       pq.add(new int[] {next[0], next[1] + dist});
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            sb.append((distance[i] == INF) ? "INF" : distance[i]).append("\n");
        }
        System.out.println(sb);
    }
}
