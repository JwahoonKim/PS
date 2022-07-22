import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1256 {
    static int N, M, K;
    static StringBuilder answer = new StringBuilder();
    static int[][] pascal;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        pascal = new int[N + M][N + M];
        for (int i = 0; i < N + M; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0) pascal[i][j] = 1;
                else if (j == i) pascal[i][j] = 1;
                else {
                    pascal[i][j] = Math.min((int) 1e9, pascal[i - 1][j - 1] + pascal[i - 1][j]);
                }
            }
        }

        // 사전에 없는 단어를 원하는 경우
        if (K > pascal[N + M - 1][M - 1] + pascal[N + M - 1][M]) {
            System.out.println(-1);
            return;
        }

        // 단어 찾기
        go(N, M, K);
        System.out.println(answer);
    }

    private static void go(int n, int m, int k) {
        if (answer.length() == N + M)
            return;
        int c = pascal[n + m - 1][m];
        if (c < k) {
            answer.append("z");
            go(n, m - 1, k - c);
        } else {
            answer.append("a");
            go(n - 1, m, k);
        }
    }
}
