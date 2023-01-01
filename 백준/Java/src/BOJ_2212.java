import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_2212 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());

        int[] sensors = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            sensors[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(sensors);

        int[] dist = new int[N - 1];
        for (int i = 0; i < N - 1; i++) {
            dist[i] = sensors[i + 1] - sensors[i];
        }

        Arrays.sort(dist);
        int answer = 0;
        for (int i = 0; i < dist.length - K + 1; i++) {
            answer += dist[i];
        }

        System.out.println(answer);
    }
}
