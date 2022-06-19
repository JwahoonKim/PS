import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class BOJ_2667 {
    static ArrayList<Integer> answer = new ArrayList<>();
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static boolean[][] visited;
    static int[][] graph;
    static int count = 0;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        visited = new boolean[N][N];
        graph = new int[N][N];

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                count = 0;
                if (graph[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j);
                    answer.add(count);
                }
            }
        }

        Collections.sort(answer);
        System.out.println(answer.size());
        for (int n : answer) {
            System.out.println(n);
        }
    }

    private static void dfs(int i, int j) {

        if (visited[i][j] || graph[i][j] == 0)
            return;

        count++;
        visited[i][j] = true;

        for (int k = 0; k < 4; k ++) {
            int nx = i + dx[k];
            int ny = j + dy[k];
            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                dfs(nx, ny);
            }
        }
    }
}
