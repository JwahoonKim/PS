import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_14003 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        int[] nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> L = new ArrayList<>();
        int[] record = new int[N];
        for (int i = 0; i < N; i++) {
            int now = nums[i];
            if (L.isEmpty() || L.get(L.size() - 1) < now) {
                L.add(now);
                record[i] = L.size() - 1;
            } else {
                int idx = binarySearch(L, now);
                L.set(idx, now);
                record[i] = idx;
            }
        }

        System.out.println(L.size());

        int cnt = L.size() - 1;
        int[] answer = new int[cnt + 1];

        for (int i = N - 1; i >= 0; i--) {
            if (record[i] == cnt) {
                answer[cnt] = nums[i];
                cnt--;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i : answer) {
            sb.append(i).append(" ");
        }

        System.out.println(sb);
    }

    private static int binarySearch(List<Integer> L, int target) {
        int left = 0;
        int right = L.size() - 1;

        while(left <= right) {
            int mid = (left + right) / 2;
            int now = L.get(mid);

            if (now == target)
                return mid;
            else if (now > target)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
}
