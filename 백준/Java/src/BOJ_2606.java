import java.io.*;
import java.util.*;

public class BOJ_2606 {

    static int answer = 0;

    static void dfs(int now, boolean[] visited, List<ArrayList<Integer>> graph) {
        if (visited[now])
            return;

        visited[now] = true;
        answer++;

        for (int next : graph.get(now)) {
            dfs(next, visited, graph);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int pair = Integer.parseInt(br.readLine());

        boolean[] visited = new boolean[N + 1];

        List<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i ++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < pair; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        dfs(1, visited, graph);

        System.out.println(answer - 1);
    }
}
