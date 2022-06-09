import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_2178 {
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            String nums = br.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = nums.charAt(j) - '0';
            }
        }

        Queue<Place> q = new LinkedList<>();
        q.add(new Place(0, 0));

        while (q.size() > 0) {
            Place now = q.remove();
            int x = now.x;
            int y = now.y;
            for (int i = 0; i < 4; i ++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < N && 0 <= ny && ny < M && graph[nx][ny] == 1) {
                    q.add(new Place(nx, ny));
                    graph[nx][ny] = graph[x][y] + 1;
                }
            }
        }

        System.out.println(graph[N - 1][M - 1]);
    }

    static class Place {
        int x;
        int y;

        public Place(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
