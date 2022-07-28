import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_1865 {
    private static final int INF = (int)1e9;
    static int TC, N, M, W;
    static boolean cycle;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        TC = Integer.parseInt(br.readLine());
        for (int i = 0; i < TC; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());

            List<int[]> adj = new ArrayList<>();
            cycle = false;

            for (int j = 0; j < M; j++) {
                st = new StringTokenizer(br.readLine(), " ");
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                adj.add(new int[] {start, end, cost});
                adj.add(new int[] {end, start, cost});
            }

            for (int j = 0; j < W; j++) {
                st = new StringTokenizer(br.readLine(), " ");
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                adj.add(new int[] {start, end, -cost});
            }

            int[] distance = new int[N + 1];
            Arrays.fill(distance, INF);
            distance[1] = 0;

            for (int k = 1; k <= N; k++) {
                for (int[] path : adj) {
                    int start = path[0];
                    int end = path[1];
                    int cost = path[2];

                    if (distance[end] > distance[start] + cost) {
                        if (k == N) {
                            cycle = true;
                            break;
                        }
                        distance[end] = distance[start] + cost;
                    }
                }
            }

            System.out.println(cycle ? "YES" : "NO");
        }
    }
}
