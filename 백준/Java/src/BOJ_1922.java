import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_1922 {
    static int N, M;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(i -> i[2]));
        int connect = 0;
        int answer = 0;
        parent = new int[N + 1];
        for (int i = 0; i < N + 1; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            int[] info = new int[] {a, b, cost};
            // 경로 정보 우선순위큐에 집어넣기 (연결 비용이 적은 것 우선)
            pq.add(info);
        }

        // 큐 하나씩 빼서 연결할지 결정
        while(!pq.isEmpty() && connect < N) {
            int[] poll = pq.poll();
            int start = poll[0];
            int end = poll[1];
            int cost = poll[2];
            // 연결 조건 : 이미 연결되어있지 않은지 체크 (find-union 사용)
            if (find(start) != find(end)) {
                union(start, end);
                answer += cost;
                connect++;
            }
        }
        System.out.println(answer);
    }

    static int find(int n) {
        return parent[n] = (n == parent[n]) ? n : find(parent[n]);
    }

    static void union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);
        parent[aRoot] = bRoot;
    }
}
