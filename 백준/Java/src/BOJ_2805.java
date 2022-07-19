import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2805 {
    static int N, K;
    static long[] trees;
    static long answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        long left = 0, right = 0;
        trees = new long[N];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            right = Math.max(trees[i], right);
        }

        while (left <= right) {
            long mid = (left + right) / 2;
            long result = getTree(mid);
            if (result >= K) {
                answer = Math.max(answer, mid);
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(answer);
    }

    private static long getTree(long h) {
        return Arrays.stream(trees).map(tree -> Math.max(tree - h, 0)).sum();
    }
}
