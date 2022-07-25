import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1717 {
    static int N, M;
    static int[] parent;
    static StringBuilder answer = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        parent = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int command = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (command == 0) {
                union(a, b);
            } else {
                answer.append((find(a) == find(b)) ? "YES" : "NO").append("\n");
            }
        }

        System.out.println(answer);
    }
    private static void union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);
        parent[bRoot] = aRoot;
    }


    private static int find(int n) {
        return parent[n] = (n == parent[n]) ? n : find(parent[n]);
    }

}
