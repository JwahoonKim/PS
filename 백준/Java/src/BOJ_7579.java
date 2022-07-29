import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_7579 {
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[] apps = new int[N];
        int[] costs = new int[N];

        StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            apps[i] = Integer.parseInt(st1.nextToken());
            costs[i] = Integer.parseInt(st2.nextToken());
        }

        int sum = Arrays.stream(costs).sum();
        int[][] dp = new int[sum + 1][N];

        for (int i = 0; i <= sum; i++) {
            if (costs[0] > i)
                dp[i][0] = 0;
            else
                dp[i][0] = apps[0];
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j <= sum; j++) {
                if (costs[i] > j)
                    dp[j][i] = dp[j][i - 1];
                else
                    dp[j][i] = Math.max(dp[j - costs[i]][i - 1] + apps[i], dp[j][i - 1]);
            }
        }

        boolean find = false;
        for (int i = 0; i <= sum; i++) {
            int[] line = dp[i];
            for (int memory : line) {
                if (memory >= M) {
                    System.out.println(i);
                    find = true;
                    break;
                }
            }
            if (find)
                break;
        }
    }
}
