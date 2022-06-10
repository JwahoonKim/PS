import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2468 {
    static int[][] graph;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int answer = 1;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];

        int max = 1;
        int min = 101;

        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                int now = Integer.parseInt(s[j]);
                max = Math.max(max, now);
                min = Math.min(min, now);
                graph[i][j] = now;
            }
        }

        for (int i = min; i < max; i++) {
            answer = Math.max(answer, countSafeRegion(i));
        }

        System.out.println(answer);
    }

    private static int countSafeRegion(int h) {
        int result = 0;
        boolean[][] visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (dfs(i, j, h, visited)) {
                    result++;
                }
            }
        }
        return result;
    }

    private static boolean dfs(int x, int y, int h, boolean[][] visited) {

        if (graph[x][y] <= h || visited[x][y]) {
            visited[x][y] = true;
            return false;
        }

        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                dfs(nx, ny, h, visited);
            }
        }
        return true;
    }
}
