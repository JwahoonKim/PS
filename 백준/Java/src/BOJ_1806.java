import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1806 {
    static int N, K;
    static int[] nums;
    static int DEFAULT_ANSWER = 100_001;
    static int answer = DEFAULT_ANSWER;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        nums = new int[N];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0, right = 0;
        int sum = nums[0];

        while (true) {
            if (sum < K) {
                right++;
                if (right == N)
                    break;
                sum += nums[right];
            } else {
                answer = Math.min(answer, right - left + 1);
                sum -= nums[left++];
            }
        }

        answer = answer == DEFAULT_ANSWER ? 0 : answer;
        System.out.println(answer);
    }
}
