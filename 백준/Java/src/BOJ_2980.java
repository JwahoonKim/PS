import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2980 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[][] traffic = new int[L + 1][2];
        for (int i = 0; i < N; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
            int place = Integer.parseInt(st1.nextToken());
            traffic[place][0] = Integer.parseInt(st1.nextToken());
            traffic[place][1] = Integer.parseInt(st1.nextToken());
        }

        int T = 0;
        int now = 0;
        while (now != L) {
            if (traffic[now][0] != 0) {
                int red = traffic[now][0];
                int green = traffic[now][1];
                int sum = red + green;

                while(T % sum < red)
                    T++;
            }
            now++;
            T++;
        }

        System.out.println(T);
    }
}
