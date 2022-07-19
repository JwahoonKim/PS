import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1072 {
    static double X, Y;
    static long answer = 1_000_000_001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        X = Double.parseDouble(st.nextToken());
        Y = Double.parseDouble(st.nextToken());

        int winRate = (int)(Y * 100 / X);

        if (winRate >= 99) {
            System.out.println(-1);
            return;
        }

        int left = 1, right = 1_000_000_000;
        while (left <= right) {
            int mid = (left + right) / 2;
            double ny = Y + mid, nx = X + mid;
            int changed = (int)(ny * 100 / nx);
            if (changed > winRate) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }
}
