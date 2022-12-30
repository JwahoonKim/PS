import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1182 {
    static int answer = 0;
    static int N;
    static int S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        go(0, 0, nums);
        System.out.println(answer);
    }

    private static void go(int cursor, int sum, int[] nums) {
        if (cursor >= N)
            return;

        if (sum + nums[cursor] == S)
            answer++;

        go(cursor + 1, sum, nums);
        go(cursor + 1, sum + nums[cursor], nums);
    }
}
