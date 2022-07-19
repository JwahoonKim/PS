import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_2003 {
    static int N, M;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st1.nextToken());
        M = Integer.parseInt(st1.nextToken());

        List<Integer> nums = new ArrayList<>();

        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i <N; i++) {
            nums.add(Integer.parseInt(st2.nextToken()));
        }

        int left = 0;
        int right = 0;
        int sum = nums.get(0);

        while (true) {
            if (sum == M) {
                answer ++;
                sum -= nums.get(left++);
            } else if (sum < M) {
                right++;
                if (right == N)
                    break;
                sum += nums.get(right);
            } else {
                sum -= nums.get(left++);
            }
        }

        System.out.println(answer);
    }
}
