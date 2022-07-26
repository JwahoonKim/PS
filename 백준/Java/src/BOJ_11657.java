import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_11657 {
    static long N, M;
    static final long INF = Integer.MAX_VALUE;
    static boolean cycle = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        long[] distance = new long[(int) (N + 1)];
        Arrays.fill(distance, INF);
        distance[1] = 0;

        long[][] path = new long[(int) M][3];
        for (long i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            long start = Integer.parseInt(st.nextToken());
            long end = Integer.parseInt(st.nextToken());
            long cost = Integer.parseInt(st.nextToken());
            path[(int) i] = new long[] {start, end, cost};
        }

        for (long i = 0; i < N; i++) {
            for (long j = 0; j < M; j++) {
                long[] now = path[(int) j];
                long start = now[0];
                long end = now[1];
                long cost = now[2];

                if (distance[(int) start] != INF && distance[(int) start] + cost < distance[(int) end]) {
                    distance[(int) end] = distance[(int) start] + cost;
                    if (i == N - 1) {
                        cycle = true;
                    }
                }
            }
        }

        if (cycle)
            System.out.println(-1);
        else
            for (long i = 2; i <= N; i++)
                System.out.println(distance[(int) i] == INF ? -1 : distance[(int) i]);
    }
}
