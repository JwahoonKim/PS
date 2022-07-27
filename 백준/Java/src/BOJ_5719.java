import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_5719 {
    private static final int INF = Integer.MAX_VALUE;
    static int N, M;
    static int S, D;
    static int[] distance;
    static int[][] adj;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            if (N == 0 && M == 0) {
                System.out.println(sb);
                break;
            }

            adj = new int[N][N];
            distance = new int[N];
            Arrays.fill(distance, INF);

            st = new StringTokenizer(br.readLine(), " ");
            S = Integer.parseInt(st.nextToken());
            D = Integer.parseInt(st.nextToken());

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                int dist = Integer.parseInt(st.nextToken());
                adj[start][end] = dist;
            }

            // 지금, 비용, 경로
            dijkstra(S);
            removeShortest(S, D);
            distance = new int[N];
            Arrays.fill(distance, INF);
            dijkstra(S);

            sb.append(distance[D] != INF ? distance[D] : -1).append("\n");

        }
    }

    private static void dijkstra(int s) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        pq.add(new int[] {s, 0});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int node = poll[0];
            int cost = poll[1];

            if (distance[node] != INF)
                continue;
            distance[node] = cost;

            for (int i = 0; i < N; i++) {
                if (adj[node][i] != 0) {
                    pq.add(new int[] {i, cost + adj[node][i]});
                }
            }
        }
    }

    private static void removeShortest(int s, int d) {
        if (s == d)
            return;

        for (int i = 0; i < N; i++) {
            if (adj[i][d] != 0) {
                if (distance[d] - adj[i][d] == distance[i]) {
                    adj[i][d] = 0;
                    removeShortest(s, i);
                }
            }
        }
    }
}
