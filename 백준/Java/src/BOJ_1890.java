import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1890 {
    static int[][] graph;
    static long[][] dp;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        dp = new long[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = 1L;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int step = graph[i][j];
                long acc = dp[i][j];

                if (i == N - 1 && j == N - 1)
                    break;

                if (i + step < N)
                    dp[i + step][j] += acc;

                if (j + step < N)
                    dp[i][j + step] += acc;
            }
        }

        System.out.println(dp[N - 1][N - 1]);
    }
}
