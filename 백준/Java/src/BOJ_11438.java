import java.awt.image.Kernel;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_11438 {
    static int N, M;
    static int[] depth;
    static int maxDepth;
    static int[][] parent;
    static StringBuilder sb = new StringBuilder();
    static List<List<Integer>> tree = new ArrayList<>();


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i <= N; i++) {
            tree.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tree.get(a).add(b);
            tree.get(b).add(a);
        }

        depth = new int[N + 1];
        maxDepth = 1;
        int cnt = 1;
        while (cnt < N) {
            cnt *= 2;
            maxDepth++;
        }

        parent = new int[N + 1][maxDepth];
        dfs(1, 1); // tree의 depth와 직계 부모 정보 넣기
        fillParents();

        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            LCA(a, b);
        }
        System.out.println(sb);
    }

    private static void dfs(int node, int d) {
        depth[node] = d;
        for (int next : tree.get(node)) {
            if (depth[next] == 0) {
                dfs(next, d + 1);
                parent[next][0] = node;
            }
        }
    }

    private static void fillParents() {
        for (int i = 1; i < maxDepth; i++) {
            for (int j = 1; j <= N; j++) {
                parent[j][i] = parent[parent[j][i - 1]][i - 1];
            }
        }
    }

    private static void LCA(int a, int b) {
        // a가 depth가 큰 숫자로 변경
        if (depth[a] < depth[b]) {
            int tmp = a;
            a = b;
            b = tmp;
        }

        // a와 b의 depth 맞추기
        for (int i = maxDepth - 1; i >= 0; i--) {
            if(Math.pow(2, i) <= depth[a] - depth[b]) {
                a = parent[a][i];
            }
        }

        if (a == b) {
            sb.append(a).append("\n");
            return;
        }

       // depth가 같으니 조상 찾기
        for (int i = maxDepth - 1; i >= 0; i--) {
            if (parent[a][i] != parent[b][i]) {
                a = parent[a][i];
                b = parent[b][i];
            }
        }
        a = parent[a][0];
        sb.append(a).append("\n");
    }
}
