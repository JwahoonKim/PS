import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_6236 {
    static int N;
    static int M;
    static int[] plan;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        plan = new int[N];
        for (int i = 0; i < N; i++) {
            plan[i] = Integer.parseInt(br.readLine());
        }

        int left = 0;
        int right = 100_000 * 10_000;
        int answer = right;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (isValid(mid)) {
                answer =  mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }

    private static boolean isValid(int K) {
        int count = 1;
        int money = K;

        for (int i = 0; i < N; i++) {
            int today = plan[i];
            if (today > K) return false;

            if (today > money) {
                if (++count > M) return false;
                money = K;
            }
            money -= today;
        }
        return true;
    }
}
