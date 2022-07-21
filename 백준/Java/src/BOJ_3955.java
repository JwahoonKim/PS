import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3955 {
    static int t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            long K = Integer.parseInt(st.nextToken());
            long C = Integer.parseInt(st.nextToken());

            long[] result = func(K, C);
            long x0 = -result[0];
            long y0 = result[1];
            long r0 = result[2];
            if (r0 != 1) {
                System.out.println("IMPOSSIBLE");
            } else {
                long k = 0;
                while (true) {
                    long x1 = x0 + C * k;
                    long y1 = y0 + K * k;

                    if (y1 > 1_000_000_000 || x1 > 1_000_000_000) {
                        System.out.println("IMPOSSIBLE");
                        break;
                    }

                    if (x1 > 0 && y1 > 0) {
                        System.out.println(y1);
                        break;
                    }
                    k++;
                }
            }
        }
    }

    static long[] func(long a, long b) {
        long s0 = 1, s1 = 0;
        long t0 = 0, t1 = 1;
        long r0 = a, r1 = b;

        while (r1 != 0) {
            long q = r0 / r1;
            long r = r0 - r1 * q;
            long s = s0 - s1 * q;
            long t = t0 - t1 * q;

            s0 = s1; s1 = s;
            t0 = t1; t1 = t;
            r0 = r1; r1 = r;
        }

        return new long[] {s0, t0, r0};
    }
}
