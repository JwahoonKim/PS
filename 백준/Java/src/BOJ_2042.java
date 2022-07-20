import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2042 {
    static int N, M, K, S;
    static long[] nums, tree;
    static final int UPDATE = 1;
    static final int QUERY = 2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt((st.nextToken()));
        M = Integer.parseInt((st.nextToken()));
        K = Integer.parseInt((st.nextToken()));
        S = 1;

        while (S < N) {
            S *= 2;
        }

        nums = new long[S];
        tree = new long[2 * S];

        for (int i = 0; i < N; i++) {
            nums[i] = Long.parseLong(br.readLine());
        }

        initTree();

        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if (a == UPDATE) {
                update(1, S, 1, b, c - tree[S + b - 1]);
            }

            if (a == QUERY) {
                System.out.println(query(1, S, 1, b, (int) c));
            }
        }
    }

    private static void initTree() {
        for (int i = 0; i < S; i++) {
            tree[S + i] = nums[i];
        }

        for (int i = S - 1; i > 0; i--) {
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }
    }

    private static long query(int left, int right, int node, int queryLeft, int queryRight) {
        // 연관 없음
        if (queryRight < left || queryLeft > right) {
            return 0;
        }
        // 판단 가능
        else if (queryLeft <= left && right <= queryRight) {
            return tree[node];
        }
        // 판단 불가 -> 자식에게 위임
        else {
            int mid = (left + right) / 2;
            long leftResult = query(left, mid, node * 2, queryLeft, queryRight);
            long rightResult = query(mid + 1, right, node * 2 + 1, queryLeft, queryRight);
            return leftResult + rightResult;
        }
    }

    private static void update (int left, int right, int node, int target, long diff) {
        // 연관 없음
        if (right < target || target < left) {
            return;
        }
        // 연관 있음 => 자식에게도 전파
        else {
            tree[node] += diff;
            if (left != right) {
                int mid = (left + right) / 2;
                update(left, mid, node * 2, target, diff);
                update(mid + 1, right, node * 2 + 1, target, diff);
            }
        }
    }
}

