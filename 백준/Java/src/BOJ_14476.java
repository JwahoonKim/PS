import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14476 {
    static int N;
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] leftToRight = new int[N];
        int[] rightToLeft = new int[N];

        leftToRight[0] = nums[0];
        rightToLeft[N - 1] = nums[N - 1];

        for (int i = 1; i < N; i++) {
            leftToRight[i] = gcd(leftToRight[i - 1], nums[i]);
        }

        for (int i = N - 2; i >= 0; i--) {
            rightToLeft[i] = gcd(rightToLeft[i + 1], nums[i]);
        }

        int answer = 1;
        int exclude = 0;

        for (int i = 0; i < N; i++) {
            int gcd;
            if (i == 0) {
                gcd = rightToLeft[i + 1];
            } else if (i == N - 1) {
                gcd = leftToRight[i - 1];
            } else {
                gcd = gcd(leftToRight[i - 1], rightToLeft[i + 1]);
            }
            if (answer < gcd) {
                answer = gcd;
                exclude = nums[i];
            }
        }

        if (exclude == 0 || (exclude % answer) == 0) {
            System.out.println(-1);
        } else {
            System.out.println(answer + " " + exclude);
        }
    }


    static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
