import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class BOJ_11057 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int N = sc.nextInt();

        long[][] dp = new long[N + 1][10];
        Arrays.fill(dp[1], 1);

        for (int i = 2; i <= N; i++) {
            for (int j = 0; j < 10; j++) {
                long sum = 0;
                for (int k = j; k < 10; k++) {
                    sum += dp[i - 1][k];
                }
                dp[i][j] = sum % 10007;
            }
        }

        long answer = Arrays.stream(dp[N], 0, 10).sum();
        System.out.println(answer % 10007);
    }
}
