import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_2644 {

    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int answer = -1;

    public static void main(String[] args) throws IOException {

        // 입력부
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        visited = new boolean[n + 1];

        StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
        int p1 = Integer.parseInt(st1.nextToken());
        int p2 = Integer.parseInt(st1.nextToken());

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st2.nextToken());
            int y = Integer.parseInt(st2.nextToken());
            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        // 로직 시작
        bfs(p1, p2, 0);

        System.out.println(answer);
    }

    private static void bfs(int now, int target, int depth) {
        if (now == target) {
            answer = depth;
        }

        visited[now] = true;

        ArrayList<Integer> nexts = graph.get(now);
        for (int next : nexts) {
            if (!visited[next])
                bfs(next, target, depth + 1);
        }
    }
}
