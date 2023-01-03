import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1743 {
    static int[][] arr;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int N;
    static int M;
    static int answer = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        initArr(br, N, M, K);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 1)
                    answer = Math.max(dfs(i, j, 0), answer);
            }
        }

        System.out.println(answer);
    }

    private static int dfs(int r, int c, int size) {
        int result = 1;
        arr[r][c] = -1;
        for (int i = 0; i < 4; i++) {
            int dr = r + dx[i];
            int dc = c + dy[i];
            if (0 <= dr && dr < N && 0 <= dc && dc < M ) {
                if (arr[dr][dc] == 1) {
                    result += dfs(dr, dc, 0);
                }
            }
        }
        return result;
    }

    private static void initArr(BufferedReader br, int N, int M, int K) throws IOException {
        arr = new int[N][M];
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            arr[r][c] = 1;
        }
    }
}
