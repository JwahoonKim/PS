import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_3176 {
    static int N, K;
    static int maxDepth;
    static int INF = 1_000_001;
    static List<List<int[]>> tree = new ArrayList<>();
    static int[] depth;
    static int[][] parent;
    static int[][] maxCost;
    static int[][] minCost;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 입력 -> 트리 설정
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i <= N; i++) {
            tree.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            tree.get(a).add(new int[]{b, cost});
            tree.get(b).add(new int[]{a, cost});
        }

        maxDepth = 0;
        int cnt = 1;
        while(cnt < N) {
            cnt *= 2;
            maxDepth++;
        }

        depth = new int[N + 1];
        parent = new int[N + 1][maxDepth];
        maxCost = new int[N + 1][maxDepth];
        minCost = new int[N + 1][maxDepth];
        for (int i = 0; i <= N; i++) {
            Arrays.fill(minCost[i], INF);
        }

        // 1차 부모 설정 DFS
        dfs(1, 1);
        fillParents();
        fillMinCost();
        fillMaxCost();

        // 입력 -> LCA
        K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            LCA(a, b);
        }
    }

    private static void LCA(int a, int b) {
        if (depth[a] < depth[b]) {
            int tmp = b;
            b = a;
            a = tmp;
        }
        
        int aStart = a, bStart = b;
        int LCA;
        int aMax = 0, bMax = 0;
        int aMin = INF, bMin = INF;
        
        // depth 맞춰주기
        for (int i = maxDepth - 1; i >= 0; i--) {
            if (Math.pow(2, i) <= depth[a] - depth[b]) {
                a = parent[a][i];
            }
        }

        // 공통조상 바로 찾아진 경우
        if (a == b) {
            LCA = a;
        } else {
            // 공통조상 찾으러가기
            for (int i = maxDepth - 1; i >= 0; i--) {
                if (parent[a][i] != parent[b][i]) {
                    a = parent[a][i];
                    b = parent[b][i];
                }
            }
            LCA = parent[a][0];
        }

        for (int i = maxDepth - 1; i >= 0; i--) {
            if (Math.pow(2, i) <= depth[aStart] - depth[LCA]) {
                aMin = Math.min(aMin, minCost[aStart][i]);
                aMax = Math.max(aMax, maxCost[aStart][i]);
                aStart = parent[aStart][i];
            }
        }

        for (int i = maxDepth - 1; i >= 0; i--) {
            if (Math.pow(2, i) <= depth[bStart] - depth[LCA]) {
                bMin = Math.min(bMin, minCost[bStart][i]);
                bMax = Math.max(bMax, maxCost[bStart][i]);
                bStart = parent[bStart][i];
            }
        }

        int MIN = Math.min(aMin, bMin);
        int MAX = Math.max(aMax, bMax);

        System.out.println(MIN + " " + MAX);
    }

    private static void fillMaxCost() {
        for (int i = 1; i < maxDepth; i++) {
            for (int j = 1; j <= N; j++) {
                maxCost[j][i] = Math.max(maxCost[j][i - 1], maxCost[parent[j][i - 1]][i - 1]);
            }
        }
    }

    private static void fillMinCost() {
        for (int i = 1; i < maxDepth; i++) {
            for (int j = 1; j <= N; j++) {
                minCost[j][i] = Math.min(minCost[j][i - 1], minCost[parent[j][i - 1]][i - 1]);
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
    
    

    private static void dfs(int node, int d) {
        depth[node] = d;

        for (int[] next : tree.get(node)) {
            if (depth[next[0]] == 0) {
                dfs(next[0], d + 1);
                parent[next[0]][0] = node;
                maxCost[next[0]][0] = next[1];
                minCost[next[0]][0] = next[1];
            }
        }
    }
}
