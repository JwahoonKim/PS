import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2563 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] paper = new int[101][101];
        for (int i = 0; i < N; i++) {
            String[] nums = br.readLine().split(" ");
            int x = Integer.parseInt(nums[0]);
            int y = Integer.parseInt(nums[1]);

            for (int j = 0; j < 10; j ++) {
                int nx = x + j;
                for (int k = 0; k < 10; k ++) {
                    int ny = y + k;
                    paper[ny][nx] = 1;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < 101; i ++) {
            for (int j = 0; j < 101; j ++) {
                if (paper[i][j] == 1) count ++;
            }
        }

        System.out.println(count);
    }
}
