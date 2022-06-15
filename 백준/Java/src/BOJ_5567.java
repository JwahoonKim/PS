import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_5567 {
    static int answer = -1;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        boolean[] visited = new boolean[N + 1];
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {1, 0});

        while (q.size() > 0) {
            int[] now = q.poll();
            int person = now[0];
            int depth = now[1];

            if (visited[person]) continue;
            visited[person] = true;
            answer++;

            ArrayList<Integer> people = graph.get(person);
            for (int next : people) {
                if (depth + 1 <= 2 && !visited[next]) {
                    q.add(new int[]{next, depth + 1});
                }
            }
        }

        System.out.println(answer);
    }
}
