import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2243 {
    static int S, n;
    static long[] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        S = 1;
        while (S < 1_000_000) {
            S *= 2;
        }

        tree = new long[2 * S];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int type = Integer.parseInt(st.nextToken());
            if (type == 1) {
                // 사탕 빼기 및 출력 -> query + print + update
                long rank = Long.parseLong(st.nextToken());
                int candy = pick(1, rank);
                System.out.println(candy);
            } else {
                // 사탕 수 조작(넣기 혹은 빼기) -> update
                int flavor = Integer.parseInt(st.nextToken());
                long count = Integer.parseInt(st.nextToken());
                update(1, S, 1, flavor, count);
            }
        }
    }

    private static void update(int left, int right, int node, int flavor, long count) {
        // 업데이트 할 곳이 아닌 경우
        if (flavor < left || right < flavor) {
            return;
        }
        // 업데이트 할 곳인 경우
        else {
            tree[node] += count;
            // 마지막 노드인지 체크
            if (left != right) {
                int mid = (left + right) / 2;
                update(left, mid, node * 2, flavor, count);
                update(mid + 1, right, node * 2 + 1, flavor, count);
            }
        }
    }

    private static int pick(int node, long rank) {
        if (S <= node) {
            update(1, S, 1, node - S + 1, -1);
            return node - S + 1;
        }
        // 좌측으로 갈 수 있는지 체크해보기
        long leftCount = tree[node * 2];

        if (rank <= leftCount) {
            return pick(node * 2, rank);
        } else {
            return pick(node * 2 + 1, rank - leftCount);
        }
    }
}
